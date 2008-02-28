from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    profile_text = models.TextField(blank=True)
    url = models.URLField(blank=True, verify_exists=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
    
    def __str__(self):
        return self.user.username
    
    class Admin:
        pass