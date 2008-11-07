from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from timezones.fields import TimeZoneField

class Account(models.Model):
    
    user = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    
    timezone = TimeZoneField(_('timezone'))
    language = models.CharField(_('language'), max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    
    def __unicode__(self):
        return self.user.username


class OtherServiceInfo(models.Model):
    
    # eg blogrss, twitter_user, twitter_password, pownce_user, pownce_password
    
    user = models.ForeignKey(User, verbose_name=_('user'))
    key = models.CharField(_('Other Service Info Key'), max_length=50)
    value = models.TextField(_('Other Service Info Value'))
    
    class Meta:
        unique_together = [('user', 'key')]
    
    def __unicode__(self):
        return u"%s for %s" % (self.key, self.user)

def other_service(user, key, default_value=""):
    """
    retrieve the other service info for given key for the given user.
    
    return default_value ("") if no value.
    """
    try:
        value = OtherServiceInfo.objects.get(user=user, key=key).value
    except OtherServiceInfo.DoesNotExist:
        value = default_value
    return value

def update_other_services(user, **kwargs):
    """
    update the other service info for the given user using the given keyword args.
    
    e.g. update_other_services(user, twitter_user=..., twitter_password=...)
    """
    for key, value in kwargs.items():
        info, created = OtherServiceInfo.objects.get_or_create(user=user, key=key)
        info.value = value
        info.save()

def create_account(sender, instance=None, **kwargs):
    if instance is None:
        return
    account, created = Account.objects.get_or_create(user=instance)

post_save.connect(create_account, sender=User)
