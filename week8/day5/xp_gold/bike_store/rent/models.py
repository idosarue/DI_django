from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import pytz
# Create your models here.


class Address(models.Model):
    address = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.address}'

class RentalStation(models.Model):
    name = models.CharField(max_length=80)
    capacity = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=CASCADE)

class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    address = models.ForeignKey(Address,max_length=30,related_name='home_address', on_delete=CASCADE, default=1)
    city = models.ForeignKey(Address,max_length=30,related_name='city_address', on_delete=CASCADE, default=1)
    country = models.ForeignKey(Address,max_length=30, related_name='country_address', on_delete=CASCADE, default=1)


class VehicleType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    real = models.IntegerField(default=500)
    size = models.ForeignKey(VehicleSize, on_delete=models.PROTECT)


class Rental(models.Model):
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=PROTECT)

    
    def is_returned(self):
        if self.return_date:
            return True
        else:
            return False

    def rentable(self):
        if self.is_returned:
            return True
        else:
            return False

class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=PROTECT)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=PROTECT)

class VehicleAtRentalStation(models.Model):
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField(null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=PROTECT)
    station = models.ForeignKey(RentalStation, on_delete=PROTECT, default=1)
