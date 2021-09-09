from django.contrib import admin
from tickets.models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("code", "bug", "created", "assignee", "due", "status", "severity")


admin.site.register(Ticket, TicketAdmin)
