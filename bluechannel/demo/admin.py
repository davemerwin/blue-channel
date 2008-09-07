from django.contrib import admin
from bluechannel.demo.models import Step, Demo

class StepAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    pass

admin.site.register(Step, StepAdmin)

class DemoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    pass

admin.site.register(Demo, DemoAdmin)