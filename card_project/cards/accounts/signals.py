
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Topic, User
# from trading.models import Card
import random


@receiver(post_save, sender=Profile)
def create_user(sender,instance , created, **kwargs):
    if created:
        # cards = Card
        print(instance)
        # instance.deck.add(*cards)
