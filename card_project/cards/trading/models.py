from accounts.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
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

    def __str__(self):
        return self.name

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

TRADE_CHOICES = [
    ('A', 'ACCEPT'),
    ('R', 'REJECT'),
    ('P','PENDING')
]

class Transaction(models.Model):
    trade_sender = models.ForeignKey('accounts.Profile', on_delete=CASCADE, related_name='my_offer')
    trade_reciever = models.ForeignKey('accounts.Profile', related_name='offer_target',  on_delete=CASCADE, null=True)
    card = models.ForeignKey(Card, on_delete=CASCADE, related_name='trades', default=1)
    choice = models.CharField(choices=TRADE_CHOICES, default='P', max_length=10) 
    trade_choice = models.BooleanField(null=True)

class TransactionResponse(models.Model):
    trade_sender = models.ForeignKey('accounts.Profile', on_delete=CASCADE, related_name='trade_sender')
    trade_reciever = models.ForeignKey('accounts.Profile', related_name='trade_reciever',  on_delete=CASCADE, null=True)
    card = models.ForeignKey(Card, on_delete=CASCADE, related_name='trades_respone', default=1)
    original_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    trade_choice = models.BooleanField(null=True)


    def swap_cards(self):
        if self.original_transaction.trade_choice and self.trade_choice:
            return True
        else:
            return False
