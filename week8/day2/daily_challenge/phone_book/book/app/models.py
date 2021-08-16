from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20, default='john')
    email = models.EmailField(max_length=30, unique=True)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    address = models.CharField(max_length=20)