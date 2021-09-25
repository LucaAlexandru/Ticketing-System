from django.contrib import admin
from tickets.models import Ticket, Comments


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("code", "bug", "created", "assignee", "due", "status", "severity")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "ticket")


admin.site.register(Comments, CommentAdmin)
admin.site.register(Ticket, TicketAdmin)