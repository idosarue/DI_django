from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class VehicleType(models.Model):
    name = models.CharField(max_length=40)


class VehicleSize(models.Model):
    name = models.CharField(max_length=40)

class Vehicle(models.Model):
    vehicle = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    date = models.DateField()
    real = models.IntegerField()
    size = models.ForeignKey(VehicleSize, on_delete=models.PROTECT)

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(null=True)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=PROTECT)

    def is_returned(self):
        if not self.return_date:
            return False
        else:
            return True

    def rentable(self):
        if self.is_returned:
            return True
        else:
            return False
class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=PROTECT)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=PROTECT)