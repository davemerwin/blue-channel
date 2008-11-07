from datetime import datetime
from django.db import models
from tagging.fields import TagField
from django.utils.translation import ugettext_lazy as _

class Type(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'))

    class Meta:
        verbose_name_plural = ('Type')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/media-type/%i/" % (self.slug)
        
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Type, self).save(force_insert, force_update)
        

class Media(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    media_type = models.ForeignKey(Type, blank=True, null=True)
    media_file = models.FileField(upload_to='%Y/%m/%d/', max_length=255, blank=True)
    media_embed = models.TextField(blank=True, help_text="Place your EMBED code here from YouTube, Flickr or others.")
    title_text = models.CharField(blank=True, max_length=100)
    alt_text = models.CharField(blank=True, max_length=100)
    caption = models.CharField(blank=True, max_length=200)
    author = models.CharField(blank=True, max_length=100)
    liscense_type = models.CharField(blank=True, max_length=100)
    liscense_url = models.URLField(blank=True, verify_exists=True)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'))
    display = models.BooleanField(default=True)
    tags = TagField()
    
    class Meta:
        verbose_name_plural = ('Media')

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Media, self).save(force_insert, force_update)
    
    def get_absolute_url(self):
        return self.get_media_file_url()
        
    def _save_FIELD_file(self, field, filename, raw_contents, save=True):
        original_upload_to = field.upload_to
        field.upload_to = '%s/%s' % (self.media_type, field.upload_to)
        super(Media, self)._save_FIELD_file(field, filename, raw_contents, save)
        field.upload_to = original_upload_to