from accounts.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
import random
from django import forms

class Card(models.Model):
    CARD_CHOICES = [
        ('P', 'People Card'),
        ('V', 'Vehicle Card')
    ]
    name = models.CharField(max_length=50,  default=1)
    c_type = models.CharField(choices=CARD_CHOICES, max_length=2)
    owners = models.ManyToManyField('accounts.Profile', related_name='deck')
    rarity = models.IntegerField(default=0)
    price = models.IntegerField(default=50)
    min_score_buy = models.IntegerField(default=200)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    @classmethod
    def deal(cls):
        vehicle_cards = cls.objects.filter(c_type='V', quantity=1).order_by('rarity')
        people_cards = cls.objects.filter(c_type='P', quantity=1).order_by('rarity')
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
    ('P','PENDING'),
    ('C', 'COMPLETED')
]

class Transaction(models.Model):
    trade_sender = models.ForeignKey('accounts.Profile', on_delete=CASCADE, related_name='my_offer')
    trade_reciever = models.ForeignKey('accounts.Profile', related_name='offer_target',  on_delete=CASCADE, null=True)
    card = models.ForeignKey(Card, on_delete=CASCADE, related_name='card1', default=1)
    choice = models.CharField(choices=TRADE_CHOICES, default='P', max_length=10) 
    trade_choice = models.BooleanField(null=True)
    timestamp = models.DateTimeField(auto_now=True)


class TransactionResponse(models.Model):
    card = models.ForeignKey(Card, on_delete=CASCADE, related_name='trades_respone', default=1)
    original_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    trade_choice = models.BooleanField(null=True)

    def swap_cards(self):
        if self.original_transaction.trade_choice and self.trade_choice:
            self.original_transaction.choice = "C"
            return True
        else:
            return False

class SellCardTransaction(models.Model):
    seller = models.ForeignKey('accounts.Profile', on_delete=CASCADE, related_name='seller')
    buyer = models.ForeignKey('accounts.Profile', related_name='buyer',  on_delete=CASCADE, null=True)
    card = models.ForeignKey(Card, on_delete=CASCADE, related_name='card_sell', default=1)
    choice = models.CharField(choices=TRADE_CHOICES, default='P', max_length=10) 
    trade_choice = models.BooleanField(null=True)
    timestamp = models.DateTimeField(auto_now=True)
