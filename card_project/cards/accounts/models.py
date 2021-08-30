from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=PROTECT, default=1)

    def __str__(self):
        return f'{self.user}'



class Topic(models.Model):
    topic = models.CharField(max_length=4)

    def __str__(self):
        return self.topic
