from django.contrib import admin
from bluechannel.customers.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved', 'created_at','updated_at',)
    list_filter = ('approved',)
    pass

admin.site.register(Customer, CustomerAdmin)