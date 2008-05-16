import datetime
from django.db import models

class Template(models.Model):
    """
    If Page specifies a template, this is the template that is used to render
    the page.  Template files are based on the slugified name.
    """
    name = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    class Admin:
        list_filter = ('name',)
        save_on_top = True
        search_fields = ('name', 'description',)

    def save(self):
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        super(Template, self).save()

    