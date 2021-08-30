from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
import random
# class PeopleCard(models.Model):
#     name = models.CharField(max_length=50)
#     height  = models.CharField(max_length=50)
#     home_world = models.CharField(max_length=50)
#     mass = models.CharField(max_length=50)

# class VehicleCard(models.Model):
#     name = models.CharField(max_length=50)
#     model   = models.CharField(max_length=50)
#     vehicle_class  = models.CharField(max_length=50)
#     max_atmosphering_speed = models.CharField(max_length=50)


class Card(models.Model):
    CARD_CHOICES = [
        ('P', 'People Card'),
        ('V', 'Vehicle Card')
    ]
    name = models.CharField(max_length=50,  default=1)
    c_type = models.CharField(choices=CARD_CHOICES, max_length=2)
    owners = models.ManyToManyField('accounts.Profile', related_name='deck')
    rarity = models.IntegerField(default=0)

    # @classmethod
    # def deal(cls):
    #     cards = cls.objects.all().order_by('rarity')
    #     vehicle_cards = VehicleCard.objects.all().order_by('max_atmosphering_speed')
    #     a = vehicle_cards.count() / 10
    #     for i in cards:
    #         if i.c_type == "V":
    #             print(i)h
    #     print(a)
    #     return vehicle_cards

class PeopleCard(Card):
    height  = models.IntegerField()
    home_world = models.CharField(max_length=50)
    mass = models.IntegerField()


class VehicleCard(Card):
    model   = models.CharField(max_length=50)
    vehicle_class  = models.CharField(max_length=50)
    max_atmosphering_speed = models.IntegerField()


# c = Card.objects.get(id=1)
# VehicleCard.objects.create(name=, c_type='V',  )
# if c.c_type == 'P'
#     c.peoplecard
# else:
#     c.vehiclecard