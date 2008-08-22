from datetime import datetime
from django.db import models

class Template(models.Model):
    """
    If Page specifies a template, this is the template that is used to render
    the page.  Template files are based on the slugified name.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def save(self):
        if not self.id:
            self.created = datetime.now()
        self.modified = datetime.now()
        super(Template, self).save() 