from django.db import models


class Ticket(models.Model):
    code = models.CharField(max_length=7)
    bug = models.CharField(max_length=50)
    created = models.DateField(null=True)
    assignee = models.CharField(max_length=50)
    due = models.DateField(null=True)
    status = models.CharField(max_length=20)
    severity = models.CharField(max_length=20)

    def __str__(self):
        return self.code