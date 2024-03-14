from django.db import models

# Create your models here.
class Customer(models.Model):
    balance = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
