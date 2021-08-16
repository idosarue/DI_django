from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=80)


class Animal(models.Model):
    name = models.CharField(default='dog', max_length=20)
    legs =  models.IntegerField(default=4)
    top_weight =  models.IntegerField(default=50)
    height =  models.IntegerField(default=50)
    speed =  models.IntegerField(default=50)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)

