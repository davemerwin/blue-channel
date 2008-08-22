from django.contrib import admin
from bluechannel.media.models import Type, Media


class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True

admin.site.register(Type, TypeAdmin)

class MediaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_filter = ('media_type',)
    list_display = ('name', 'media_type', 'title_text', 'author',)

admin.site.register(Media, MediaAdmin)