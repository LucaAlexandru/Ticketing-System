from django.contrib import admin
from tickets.models import Ticket, Comments, TicketTemplate


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("code", "bug", "created", "assignee", "due", "status", "severity")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "ticket")

class TicketTemplateAdmin(admin.ModelAdmin):
    list_display = ("color", "font")


admin.site.register(Comments, CommentAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketTemplate, TicketTemplateAdmin)