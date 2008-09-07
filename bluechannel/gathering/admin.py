from django.contrib import admin
from bluechannel.gathering.models import Topic, Gathering

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)

class GatheringAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','description',)
    search_fields = ('title','description',)

admin.site.register(Gathering, GatheringAdmin)