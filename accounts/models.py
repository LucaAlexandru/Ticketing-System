from django.db import models
from tickets.constants import STATUS_CHOICES
from django.contrib.auth.models import User


class AccountSettings(models.Model):
    background_color = models.CharField(max_length=20)
    user_country = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    zodiac_sign = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)