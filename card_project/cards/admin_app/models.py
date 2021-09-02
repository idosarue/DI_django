from django.db import models
from trading.models import Card
# Create your models here.

class Store(models.Model):
    quantity = models.IntegerField(default=1)
    store_card = models.ForeignKey(Card, on_delete=models.CASCADE)
