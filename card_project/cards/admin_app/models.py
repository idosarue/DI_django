from django.db import models
from trading.models import Card
# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=20, default='store1')
    card = models.ManyToManyField(Card, related_name='store')
