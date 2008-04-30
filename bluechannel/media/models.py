from django.db import models
import tagging
import datetime

# Create your models here.
FILE_LIST_DISPLAY = (('Yes', 'yes'), ('No', 'no'))

class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(prepopulate_from=("name",))
        
    class Meta:
        verbose_name = ('Type')
        verbose_name_plural = ('Type')
        ordering = ['-name']
        get_latest_by = ['modified']
    
    def __str__(self):
        return self.slug
        
    def get_absolute_url(self):
        return "/media-type/%i/" % self.slug

    class Admin:
        save_on_top = True
        pass
    
class Media(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    media_type = models.ForeignKey(Type, blank=True)
    media_file = models.FileField(upload_to='%Y/%m/%d/', max_length=200, blank=True)
    media_embed = models.TextField(blank=True, help_text="Place your EMBED code here from YouTube, Flickr or others.")
    list_display = models.CharField(max_length=4, choices=FILE_LIST_DISPLAY)
    alt_text = models.CharField(blank=True, max_length=100)
    title_text = models.CharField(blank=True, max_length=100)
    caption = models.CharField(blank=True, max_length=100)
    author = models.CharField(blank=True, max_length=100)
    liscense_type = models.CharField(blank=True, max_length=100)
    liscense_url = models.URLField(blank=True, verify_exists=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(prepopulate_from=("name",))
        
    class Meta:
        verbose_name = ('Media')
        verbose_name_plural = ('Media')
        ordering = ['-name', 'media_type']
        get_latest_by = ['modified']
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return self.get_media_file_url()
        
    def _save_FIELD_file(self, field, filename, raw_contents, save=True):
        original_upload_to = field.upload_to
        field.upload_to = '%s/%s' % (self.media_type, field.upload_to)
        super(Media, self)._save_FIELD_file(field, filename, raw_contents, save)
        field.upload_to = original_upload_to
    
    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)

    tags = property(_get_tags, _set_tags)
    
    class Admin:
        list_filter = ('name','media_type',)
        list_display = ['name', 'description']
        save_on_top = True
        search_fields = ['name', 'description', 'media_type']
        pass