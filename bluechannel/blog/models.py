from datetime import datetime
from tagging.fields import TagField
from django.db import models
from django.contrib.auth.models import User
from bluechannel.media.models import Media

# Published Event Manager
class PublishedEntryManager(models.Manager):
    def get_query_set(self):
        return super(PublishedEntryManager, self).get_query_set().filter(status='publish')

class Entry(models.Model):
    """
    The central Page model.  This correlates directly with the URL such that
    the URL `/about/` would be Page.objects.get(slug='about').  Pages can be
    nested heirarchically.
    """
    ENTRY_STATUS = (
        ('draft', 'Draft'),
        ('remove', 'Remove'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ENTRY_STATUS)
    main_content = models.TextField(blank=True, help_text=("You can use Markdown to format your text. To see the syntax go here: http://daringfireball.net/projects/markdown/syntax"))
    media = models.ManyToManyField(Media, blank=True)
    summary = models.TextField(blank=True)
    media = models.ManyToManyField(Media, blank=True)
    created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)
    similar_entries = models.ManyToManyField('self', blank=True, related_name='similar')
    enable_comments = models.BooleanField(default=False)
    tags = TagField()
    
    objects = models.Manager() # The default manager.
    published_objects = PublishedEntryManager() # Only published pages

    def save(self):
        if not self.id:
            self.created = datetime.now()
        self.modified = datetime.now()
        super(Entry, self).save()

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.created.strftime("%Y/%b/%d").lower(), self.slug)
        
    class Meta:
        verbose_name = ('Entry')
        verbose_name_plural = ('Entries')
