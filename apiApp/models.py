from django.db import models
from django.forms import CharField

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class storeData(models.Model):
    store = models.CharField(max_length=100)
    sales = models.CharField(max_length=100)
    no_of_orders = models.CharField(max_length=100)
    no_of_customers = models.CharField(max_length=100)


class graph(models.Model):
    dates = models.CharField(max_length=100)
    sales = models.CharField(max_length=100)
    profits = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    expected = models.CharField(max_length=100)
    o_chan = models.CharField(max_length=100)
    deposit = models.CharField(max_length=100)
    orders = models.CharField(max_length=100)