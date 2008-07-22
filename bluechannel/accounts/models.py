from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    website = models.URLField(blank=True, verify_exists=True)
    profile_text = models.TextField(blank=True)
    phone = models.PhoneNumberField(blank=True)
    mobile = models.PhoneNumberField(blank=True)
    fax = models.PhoneNumberField(blank=True)
    Address = models.TextField(blank=True)
    city = models.CharField(blank=True, max_length=200)
    state = models.USStateField(blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    mugshot = models.ImageField(upload_to="/mugshots/", height_field=100, width_field=100, blank=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
    
    def __str__(self):
        return self.user.username
    
    class Admin:
        pass