from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=PROTECT, default=1)
    score = models.IntegerField(default=0)
    coins = models.IntegerField(default=200)
    can_sell = models.BooleanField(default=True)

    def is_seller_deck_valid(self):
        if len(self.deck.all()) > 12:
            self.can_sell = True
            return self.can_sell
        else:
            self.can_sell = False
            return self.can_sell

    def __str__(self):
        return f'{self.user}'

class Topic(models.Model):
    topic = models.CharField(max_length=4)

    def __str__(self):
        return self.topic
