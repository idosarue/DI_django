from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
import random

class Card(models.Model):
    CARD_CHOICES = [
        ('P', 'People Card'),
        ('V', 'Vehicle Card')
    ]
    name = models.CharField(max_length=50,  default=1)
    c_type = models.CharField(choices=CARD_CHOICES, max_length=2)
    owners = models.ManyToManyField('accounts.Profile', related_name='deck')
    rarity = models.IntegerField(default=0)

    @classmethod
    def deal(cls):
        vehicle_cards = cls.objects.filter(c_type='V').order_by('rarity')
        people_cards = cls.objects.filter(c_type='P').order_by('rarity')
        deck = random.sample(list(vehicle_cards), k=6) + random.sample(list(people_cards), k=6)
        return deck

class PeopleCard(Card):
    height  = models.IntegerField()
    home_world = models.CharField(max_length=50)
    mass = models.IntegerField()


class VehicleCard(Card):
    model   = models.CharField(max_length=50)
    vehicle_class  = models.CharField(max_length=50)
    max_atmosphering_speed = models.IntegerField()

