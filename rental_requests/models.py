from django.db import models
from datetime import date
# Create your models here.

class RentalRequest(models.Model):
    date_start_rent=models.DateField(default=date.today)
    deta_end_rent=models.DateField(default=date.today)
    count_objects = models.PositiveIntegerField(default=0)
    comment = models.CharField()

class Transaction(models.Model):
    date = models.DateField(default=date.today)
    rent_price = models.PositiveIntegerField(default=0)
    period = models.PositiveIntegerField(default=0)

