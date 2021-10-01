from django.contrib import admin
from accounts.models import AccountSettings

# Register your models here.
class AccountSettingsAdmin(admin.ModelAdmin):
    list_display = ("background_color", "user_country", "age", "date_of_birth", "zodiac_sign", "user")

admin.site.register(AccountSettings, AccountSettingsAdmin)