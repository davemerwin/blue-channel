import datetime
from tagging.fields import TagField
from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import *
from bluechannel.structure.models import *
from bluechannel.layout.models import *


class Content(models.Model):
    """
    A piece of content that is included via Page.
    """
    
    CONTENT_STATUS = (
        ('draft', 'Draft'),
        ('remove', 'Remove'),
        ('publish', 'Publish')
    )
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=CONTENT_STATUS)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Content')
        verbose_name_plural = ('Content')

    class Admin:
        pass
    
    def save(self):
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        super(Content, self).save()
        
class Type(models.Model):
    """
    What is Type?
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ('Type')
        verbose_name_plural = ('Type')
    
    def __str__(self):
        return self.name
    
    class Admin:
        pass

class Page(models.Model):
    """
    The central Page model.  This correlates directly with the URL such that
    the URL `/about/` would be Page.objects.get(slug='about').  Pages can be
    nested heirarchically.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(prepopulate_from=('title',))
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    main_content = models.ForeignKey(Content, related_name='main_content')
    summary = models.TextField(blank=True)
    template = models.ForeignKey(Template)
    extra_content = models.ManyToManyField(Content, related_name='extra_content')
    content_hilight = models.ManyToManyField(Content, related_name='content_hilight')
    media = models.ManyToManyField(Media)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    author = models.ForeignKey(User)
    page_type = models.ForeignKey(Type)
    similar_pages = models.ManyToManyField('self', filter_interface=models.HORIZONTAL, related_name='similar')
    enable_comments = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)
    in_nav = models.BooleanField(default=False, help_text=("Does this page represent a top level link for the site? Do you want it avalable from the Nav Bar?"))
    in_site_map = models.BooleanField(default=True)
    has_next = models.BooleanField(default=False, help_text=("Does this page have a next page?"))
    tags = TagField()
    categories = models.CharField(blank=True, max_length=100)

    class Admin:
        save_on_top = True
        list_filter = ('title','author','template', 'nav_page')

    def save(self):
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        super(Page, self).save()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if not self.parent:
            return '/%s/' % (self.slug)
        page = self
        page_list = []
        while not page.parent:
            page=page.parent
            page_list.append(page.slug)
        return '/%s/' % ('/'.join(page_list))

    def get_all_children(self):
        return Page.objects.filter(parent=self.id)

    def get_all_siblings(self):
        return Page.objects.filter(parent=self.parent)
        return "/%i/" % (self.slug)

