from datetime import datetime
#from tagging.fields import TagField
from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import Media
from bluechannel.layout.models import *
from bluechannel.tag.models import Tag

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
    created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    #tags = TagField()
	tags = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Content')
        verbose_name_plural = ('Content')

    class Admin:
        save_on_top = True
        pass
    
    def save(self):
        if not self.id:
            self.created = datetime.now()
        self.modified = datetime.now()
        super(Content, self).save()
        
class Type(models.Model):
    """
    What Type it?
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
        save_on_top = True
        pass
        
class Event(models.Model):
    """The events module"""
    name = models.CharField(blank=True, max_length=200)
    event_start_date = models.DateField(blank=True)
    event_start_time = models.TimeField(blank=True)
    event_end_date = models.DateField(blank=True)
    event_end_time = models.TimeField(blank=True)
    description = models.TextField('Content', blank=True)
    summary = models.TextField(blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
    slug = models.SlugField(prepopulate_from=("name",))
    # tags = TagField()
	tags = models.ManyToManyField(Tag)
    enable_comments = models.BooleanField(default=True)

    class Admin:
        save_on_top = True
        list_display = ('name','event_start_date')
        search_fields = ('name','description')
        pass
    
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
    PAGE_STATUS = (
        ('draft', 'Draft'),
        ('remove', 'Remove'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(prepopulate_from=('title',))
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    status = models.CharField(max_length=20, choices=PAGE_STATUS)
    main_content = models.TextField(blank=True, help_text=("You can use Markdown to format your text. To see the syntax go here: http://daringfireball.net/projects/markdown/syntax"))
    summary = models.TextField(blank=True)
    template = models.ForeignKey(Template)
    extra_content = models.ManyToManyField(Content, blank=True, related_name='extra_content')
    content_hilight = models.ManyToManyField(Content, blank=True, related_name='content_hilight')
    event = models.ManyToManyField(Event, blank=True)
    media = models.ManyToManyField(Media, blank=True)
    created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)
    similar_pages = models.ManyToManyField('self', blank=True, filter_interface=models.HORIZONTAL, related_name='similar')
    enable_comments = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)
    in_nav = models.BooleanField(default=False, help_text=("Does this page represent a top level link for the site? Do you want it avalable from the Nav Bar?"))
    is_home = models.BooleanField(default=False, blank=True, help_text=("Is this the site's homepage?"))
    in_site_map = models.BooleanField(default=True)
    has_next = models.BooleanField(default=False, help_text=("Does this page have a next page?"))
    # tags = TagField()
	tags = models.ManyToManyField(Tag)
    objects = models.Manager() # The default manager.
    published_objects = PublishedPageManager() # Only published pages

    class Admin:
        save_on_top = True
        list_display = ('title', 'parent', 'status', 'summary', 'template', 'author', 'modified', 'in_nav')
        list_filter = ('author','template','status','in_nav')

    def save(self):
        if not self.id:
            self.created = datetime.now()
        self.modified = datetime.now()
        super(Page, self).save()

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
        return Page.objects.filter(parent=self.id)

    def get_all_siblings(self):
        "Gets siblings of current page only, no children of siblings."
        return Page.objects.filter(parent=self.parent)
        return "/%i/" % (self.slug)
