from django.db import models

# Create your models here.
class Template(models.Model):
    name = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    template_file = models.CharField('Template File Name', max_length=200, blank=True, help_text=("Example: 'templates/three-column.html'. If this isn't provided, the system will use 'templates/default.html'."))
    
    class Meta:
        verbose_name = ('Template')
        verbose_name_plural = ('Templates')
        ordering = ('name',)

    def __str__(self):
        return self.name

    class Admin:
        list_filter = ('name',)
        save_on_top = True
        search_fields = ['name', 'description',]
        pass