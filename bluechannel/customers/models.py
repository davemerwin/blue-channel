from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import Media
from account.models import Account
from profiles.models import Profile

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, unique=True)
    account = models.ForeignKey(Account)
    profile = models.ForeignKey(Profile)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
    
    def __str__(self):
        return self.user.username