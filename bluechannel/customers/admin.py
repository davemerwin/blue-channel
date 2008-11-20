from django.contrib import admin
from customers.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved', 'created_at',)
    list_filter = ('approved',)
    pass

admin.site.register(Customer, CustomerAdmin)