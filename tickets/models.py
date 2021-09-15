from django.db import models
from tickets.constants import STATUS_CHOICES


class Ticket(models.Model):
    code = models.CharField(max_length=7)
    bug = models.CharField(max_length=50)
    created = models.DateField(null=True)
    assignee = models.CharField(max_length=50)
    due = models.DateField(null=True)
    status = models.CharField(max_length=20)
    severity = models.CharField(max_length=20, choices=STATUS_CHOICES, default="major")

    def __str__(self):
        return self.code