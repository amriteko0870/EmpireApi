from django.db import models

# Create your models here.

class storeData(models.Model):
    store = models.CharField(max_length=100)
    sales = models.CharField(max_length=100)
    no_of_orders = models.CharField(max_length=100)
    no_of_customers = models.CharField(max_length=100)

