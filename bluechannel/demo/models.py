from datetime import datetime
from tagging.fields import TagField
from django.db import models
from django.contrib.auth.models import User
from bluechannel.page.models import Page

# Create your models here.
class Step(models.Model):
    """Individual Piece of the Demo"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    page = models.ForeignKey(Page)
    order = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/%s/" % self.slug
    
class Demo(models.Model):
    """The Complete Demo"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    steps = models.ManyToManyField(Step)
    slug = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/%s/" % self.slug

# class ModuleOrder(models.Model):
#    """(ModuleOrder description)"""