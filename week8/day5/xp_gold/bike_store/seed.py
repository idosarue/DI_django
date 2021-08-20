
import os
import django
from faker import Faker
from faker.providers.person.en import Provider
import random


fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()
from rent.models import *

def create_first_name(number):
    for _ in range(0,number):
        first_name = fake.unique.first_name()
        return first_name


def create_last_name(number):
    for _ in range(0,number):
        last_name = fake.unique.last_name()
        return last_name



def create_email(number):
    for _ in range(0,number):
        email = fake.unique.ascii_email()
        return email

def create_phone_num(number):
    for _ in range(0,number):
        phone_num = fake.unique.phone_number()
        return phone_num


def create_address(number):
    for _ in range(0,number):
        address = fake.address()
        return address


def create_city(number):
    for _ in range(0,number):
        city = fake.city()
        return city


def create_country(number):
    for _ in range(0,number):
        country = fake.country()
        return country

def create_postal_code(number):
    for _ in range(number):
        postal_address = fake.postcode()
        return postal_address

def generate_customer(num):
    for i in range(num):
        first_name = create_first_name(num)
        last_name = create_last_name(num)
        email = create_email(num)
        phone_num = create_phone_num(num)
        city = Address.objects.all()
        country = Address.objects.all()
        address = Address.objects.all()
        Customer.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_num, city=city[i], country=country[i], address=address[i])

# generate_customer(100)

def create_vehicle_type():
    names_li = ['Road Bike', 'Mountain Bike','BMX', 'Folding Bike']
    for name in names_li:
        VehicleType.objects.create(name=name)
# create_vehicle_type()

def create_vehicle_size():
    size_li = ['big', 'very big','small', 'medium']
    for name in size_li:
        VehicleSize.objects.create(name=name)
# create_vehicle_size()

def create_vehicle(num):
    size_li = VehicleSize.objects.all()
    vehicle_li = VehicleType.objects.all()
    price_li = [700, 1000, 300, 500]
    for i in range(num):
        for x in range(4):
            Vehicle.objects.create(vehicle=vehicle_li[x], date=fake.date_between(start_date='-5y', end_date='-1y'), real=price_li[x],size=size_li[x])

# create_vehicle(25)

def create_rental_rate():
    rates = [40,50,20,30]
    size_li = VehicleSize.objects.all()
    vehicle_li = VehicleType.objects.all()
    for i in range(4):
        RentalRate.objects.create(daily_rate=rates[i],vehicle_type=vehicle_li[i], vehicle_size=size_li[i])

# create_rental_rate()

def create_rentals():
    x = random.choice(range(100))
    customer = Customer.objects.all()
    vehicle = Vehicle.objects.all()
    for i in range(100):    
        Rental.objects.create(rental_date=fake.date_between(start_date='-2y', end_date='-1y'), customer=customer[i],vehicle=vehicle[i])

    for i in range(x):
        Rental.objects.filter(id=i).update(return_date=fake.date_between(start_date='-51w', end_date='-1w'))
# create_rentals()

def generate_address(num):
    for _ in range(num):
        address = create_address(num)
        address2 = create_address(num)
        city = create_city(num)
        country= create_country(num)
        postal_code = create_postal_code(num)
        Address.objects.create(address=address, address2=address2, city=city, country=country, postal_code=postal_code)
# generate_address(100)


def genereate_rental_station(num):
    for i in range(num):
        capacity = 10
        address = Address.objects.all()
        name = address
        RentalStation.objects.create(name=name[i].address, address=address[i], capacity=capacity)

# genereate_rental_station(10)
# class Address(models.Model):
#     address = models.CharField(max_length=80)
#     address2 = models.CharField(max_length=80)
#     city = models.CharField(max_length=30)
#     country = models.CharField(max_length=30)
#     postal_code = models.CharField(max_length=200)

# class RentalStation(models.Model):
#     name = models.CharField(max_length=80)
#     capacity = models.IntegerField()
#     address = models.ForeignKey(Address, on_delete=CASCADE)

