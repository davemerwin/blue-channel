from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import Media

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, unique=True)
    website = models.URLField(blank=True, verify_exists=True)
    profile_text = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=15)
    mobile = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    Address = models.TextField(blank=True)
    city = models.CharField(blank=True, max_length=200)
    state = models.CharField(blank=True, max_length=100)
    postal_code = models.IntegerField(blank=True, null=True)
    mugshot = models.ImageField(upload_to="/mugshots/", height_field=100, width_field=100, blank=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
    
    def __str__(self):
        return self.user.username