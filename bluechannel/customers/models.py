from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import Media
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, unique=True)
    approved = models.BooleanField(default=False)
    organization = models.CharField(blank=True, max_length=255)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'), blank=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
    
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Customer, self).save(force_insert, force_update)
    
    def __str__(self):
        return self.user.username
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude=('user', 'approved', 'created_at', 'updated_at',)
        
