from datetime import datetime
from tagging.fields import TagField
from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import Media
from bluechannel.categories.models import Category
from django.utils.translation import ugettext_lazy as _

# Published Event Manager
class PublishedPostManager(models.Manager):
    def get_query_set(self):
        return super(PublishedPostManager, self).get_query_set().filter(status='publish')

class Post(models.Model):
    """
    The post model for blogs
    """
    ENTRY_STATUS = (
        ('draft', 'Draft'),
        ('remove', 'Remove'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ENTRY_STATUS)
    main_content = models.TextField(blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    media = models.ManyToManyField(Media, blank=True)
    summary = models.TextField(blank=True)
    publish = models.DateTimeField(_('publish'), default=datetime.now)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'))
    author = models.ForeignKey(User)
    similar_entries = models.ManyToManyField('self', blank=True, related_name='similar')
    enable_comments = models.BooleanField(default=False)
    close_comments = models.BooleanField(default=False)
    tags = TagField()
    
    objects = models.Manager() # The default manager.
    published_objects = PublishedPostManager() # Only published posts

    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Post, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.created_at.strftime("%Y/%b/%d").lower(), self.slug)
        
    def get_month(self):
        return "/blog/%s/" % (self.created_at.strftime("%Y/%b").lower())
        
    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
        
