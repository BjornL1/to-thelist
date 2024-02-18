from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shopping_lists')

    def __str__(self):
        return self.name


class List(models.Model):
    list_name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name