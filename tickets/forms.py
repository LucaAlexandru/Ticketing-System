# from django import forms
# from tickets.models import models
#
# class CreateThingy(forms.ModelForm):
#     class Meta:
#         model = models.Ticket
#         # fields = '__all__'
#         fields = ["code", "bug", "created", "assignee", "due", "status", "severity"]

from django import forms


class TicketForm(forms.Form):
    new_code = forms.CharField(label='code', max_length=100)
    new_bug = forms.CharField(label='bug', max_length=100)
    new_created = forms.DateField(label='created')
    new_assignee = forms.CharField(label='assignee', max_length=100)
    new_due = forms.DateField(label='due')
    new_status = forms.CharField(label='status', max_length=100)
    new_severity = forms.CharField(label='severity', max_length=100)
