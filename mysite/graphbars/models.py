from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=100)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=200)

