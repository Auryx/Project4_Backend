from django.db import models

# Create your models here.
class Dice(models.Model):
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

