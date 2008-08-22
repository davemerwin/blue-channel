from django.contrib import admin
from bluechannel.layout.models import Template

class TemplateAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    save_on_top = True
    search_fields = ('name', 'description',)

admin.site.register(Template, TemplateAdmin)