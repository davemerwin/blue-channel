from django.contrib import admin
from bluechannel.accounts.models import Account, Staff

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)

class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff, StaffAdmin)