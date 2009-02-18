from datetime import datetime
from tagging.fields import TagField
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bluechannel.media.models import Media

STATUS = (
    ('draft', 'Draft'),
    ('remove', 'Remove'),
    ('publish', 'Publish')
)

class Highlight(models.Model):
    """
    A piece of content that is included via Page.
    """
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'), blank=True)
    tags = TagField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Highlight')
        verbose_name_plural = ('Highlights')
    
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Highlight, self).save(force_insert, force_update)
        
class Type(models.Model):
    """
    What Type it?
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'), blank=True)
    
    class Meta:
        verbose_name = ('Type')
        verbose_name_plural = ('Type')
    
    def __str__(self):
        return self.name
        
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Type, self).save(force_insert, force_update)
        
class Event(models.Model):
    """The events module"""
    name = models.CharField(blank=True, max_length=200)
    event_start_date = models.DateField(blank=True)
    event_start_time = models.TimeField(blank=True)
    event_end_date = models.DateField(blank=True)
    event_end_time = models.TimeField(blank=True)
    description = models.TextField('Content', blank=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'), blank=True)
    slug = models.CharField(max_length=100)
    tags = TagField()
    enable_comments = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
        
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Event, self).save(force_insert, force_update)

class Template(models.Model):
    """A template model with sample template image"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='template_images', max_length=200, blank=True)

    def __unicode__(self):
        return self.name

# Published Page Manager
class PublishedPageManager(models.Manager):
    def get_query_set(self):
        return super(PublishedPageManager, self).get_query_set().filter(status='publish')

class Page(models.Model):
    """
    The central Page model.  This correlates directly with the URL such that
    the URL `/about/` would be Page.objects.get(slug='about').  Pages can be
    nested heirarchically.
    """

    title = models.CharField(max_length=200)
    page_title = models.CharField(blank=True, max_length=200, help_text=("Use the Page Title if you want the Title of the page to be different than the Title. For Example... Title: About. Page Title: About Our Company."))
    slug = models.CharField(max_length=100)
    template = models.ForeignKey(Template, blank=True, null=True)
    page_type = models.ForeignKey(Type)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    status = models.CharField(max_length=20, choices=STATUS)
    main_content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    hilight = models.ManyToManyField(Highlight, blank=True, related_name='hilight')
    event = models.ManyToManyField(Event, blank=True)
    media = models.ManyToManyField(Media, blank=True)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'), blank=True)
    author = models.ForeignKey(User)
    similar_pages = models.ManyToManyField('self', blank=True, related_name='similar')
    enable_comments = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)
    in_nav = models.BooleanField(default=False, help_text=("Does this page represent a top level link for the site? Do you want it avalable from the Nav Bar?"))
    is_home = models.BooleanField(default=False, blank=True, help_text=("Is this the site's homepage?"))
    in_site_map = models.BooleanField(default=True)
    has_next = models.BooleanField(default=False, help_text=("Does this page have a next page?"))
    tags = TagField()
    objects = models.Manager() # The default manager.
    published_objects = PublishedPageManager() # Only published pages

    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Page, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        parents = self.get_all_parents()
        return '/%s/' % ('/'.join([p.slug for p in parents]))

    def get_all_parents(self):
        "Gets all parents going up the parent tree until a page with no parent, including itself."
        parents = []
        page = self
        while True:
            parents.insert(0, page)
            page = page.parent
            if not page:
                break
        return parents

    def get_children(self):
        "Gets children of current page, no grandchildren."
        return Page.published_objects.filter(parent=self.id)

    def get_all_siblings(self):
        "Gets siblings of current page only, no children of siblings."
        return Page.published_objects.filter(parent=self.parent)
        #return "/%i/" % (self.slug)
