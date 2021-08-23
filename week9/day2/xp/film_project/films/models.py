from django.db import models
import django.utils

from django.db.models.deletion import PROTECT
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(default=django.utils.timezone.now)
    created_in_country = models.ForeignKey(Country,related_name='country_created', on_delete=PROTECT)
    available_in_countries = models.ManyToManyField(Country)
    category =  models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __str__(self):
        return self.title

