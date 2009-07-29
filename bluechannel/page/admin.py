from django import forms
from django.contrib import admin
from bluechannel.page.models import Highlight, Type, Event, Template, Page

class HighlightAdmin(admin.ModelAdmin):
    save_on_top = True
    pass

admin.site.register(Highlight, HighlightAdmin)

class TypeAdmin(admin.ModelAdmin):
    save_on_top = True
    pass
    
admin.site.register(Type, TypeAdmin)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_display = ('name','event_start_date')
    search_fields = ('name','description')
    pass

admin.site.register(Event, EventAdmin)

class TemplateAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'description')

admin.site.register(Template, TemplateAdmin)

class TemplateModelChoiceField(forms.ModelChoiceField):
    """Based on ModelChoiceField, but using a radio button widget"""
    widget = forms.RadioSelect

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    list_display = ('title', 'page_title', 'page_type', 'status', 'summary', 'author', 'updated_at', 'in_nav', 'parent')
    list_filter = ('status', 'in_nav', 'page_type')
    search_fields = ('title', 'page_title', 'summary', 'main_content')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "template":
            kwargs['form_class'] = TemplateModelChoiceField
            return db_field.formfield(**kwargs)
        return super(PageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Page, PageAdmin)
