from django.db import models
# Create your models here.

class Store(models.Model):
    card = models.ForeignKey('trading.Card', on_delete=models.CASCADE)
