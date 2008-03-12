from django.db import models
from django.contrib.auth.models import *
from bluechannel.media.models import *
from bluechannel.structure.models import *
import tagging
import datetime

CONTENT_STATUS = (('Draft', 'draft'), ('Remove', 'remove'), ('Publish', 'publish'))

class Content(models.Model):
    name = models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Content')
        verbose_name_plural = ('Content')

    class Admin:
        pass
        
class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Admin:
        pass

class Page(models.Model):
    title = models.CharField(max_length=200)
    main_content = models.ForeignKey(Content)
    supplimental_content = models.ManyToManyField(Content, blank=True)
    summary = models.TextField(blank=True)
    template = models.ForeignKey(Template, blank=True, null=True)
    hilight_content_1 = models.ForeignKey(Content, blank=True, null=True, related_name='hilight_page_content_1', help_text="You can add content like callouts, sidebars and more.")
    hilight_content_2 = models.ForeignKey(Content, blank=True, null=True, related_name='hilight_page_content_2')
    hilight_content_3 = models.ForeignKey(Content, blank=True, null=True, related_name='hilight_page_content_3')
    hilight_content_4 = models.ForeignKey(Content, blank=True, null=True, related_name='hilight_page_content_4')
    media_1 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_1', help_text="Typically the primary media content.")
    media_1 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_1', help_text="Typically the primary media content.")
    media_2 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_2')
    media_3 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_3')
    media_4 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_4')
    media_5 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_5')
    media_6 = models.ForeignKey(Media, blank=True, null=True, related_name='page_media_6')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    section = models.ForeignKey(Section, blank=True, null=True)
    section_home = models.BooleanField(default=False, help_text="Is this the homepage for a section?")
    page_type = models.ForeignKey(Type)
    slug = models.SlugField(prepopulate_from=("title",))
    similar_pages = models.ManyToManyField("self", blank=True, filter_interface=models.HORIZONTAL, related_name="similar")
    enable_comments = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=CONTENT_STATUS)

    class Meta:
        ordering = ['-created', '-author',]
        get_latest_by = ['modified']
        verbose_name = ('Page')
        verbose_name_plural = ('Pages')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % (self.slug)

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)

    tags = property(_get_tags, _set_tags)

    class Admin:
        list_filter = ('title','author',)
        save_on_top = True
        search_fields = ['title', 'content', 'author']
        fields = (
			('Content', {'fields': ('title', 'main_content', 'summary', 'status', 'template', 'author', 'section', 'section_home', 'page_type', 'slug', 'similar_pages', 'enable_comments', 'order')}),
			('Additional Content', {'fields': ('supplimental_content_1', 'supplimental_content_2', 'supplimental_content_3', 'supplimental_content_4')}),
			('Media', {'fields': ('media_1', 'media_2', 'media_3', 'media_4', 'media_5', 'media_6')}),
			)
        pass