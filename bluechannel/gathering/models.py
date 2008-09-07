from django.db import models
from django.contrib.auth.models import User
from bluechannel.page.models import Event
from tagging.fields import TagField
        
class Topic(models.Model):
    """(Topic description)"""
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    tags = TagField()

    def __str__(self):
        return self.title

class Gathering(models.Model):
    """(Gathering description)"""
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=100)
    speakers = models.ManyToManyField(User, blank=True)
    topics = models.ManyToManyField(Topic, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    attendee = models.ManyToManyField(User, blank=True, related_name="User")
    tags = TagField()

    def __str__(self):
        return self.title