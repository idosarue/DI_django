from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT

class PeopleCard(models.Model):
    name = models.CharField(max_length=50)
    height  = models.CharField(max_length=50)
    home_world = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)

class VehicleCard(models.Model):
    name = models.CharField(max_length=50)
    model   = models.CharField(max_length=50)
    vehicle_class  = models.CharField(max_length=50)
    max_atmosphering_speed = models.CharField(max_length=50)

class Deck(models.Model):
    car_cards = models.ManyToManyField(PeopleCard)
    vehicle_cards = models.ManyToManyField(VehicleCard)

    @classmethod
    def deal(cls):
        for _ in range(6):
            