from django.contrib import admin
from bluechannel.blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    list_display = ('title', 'status', 'summary', 'author', 'modified')
    list_filter = ('status', 'author')
    search_fields = ('title', 'main_content', 'summary')

admin.site.register(Entry, EntryAdmin)