import os
import django
import json
import requests



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cards.settings')
django.setup()

from accounts.models import Topic
from trading.models import PeopleCard, VehicleCard

response_people = requests.get('https://swapi.dev/api/people')
response_vehicles = requests.get("https://swapi.dev/api/vehicles/")
people = response_people.json()['results']
vehicles = response_vehicles.json()['results']
# print(vehicles)
# for i in people:
#     print(type(i))

def create_topics():
    topic_li = ['Wookie', 'Hutt', 'Jedi', 'StormTrooper(not recommended)']
    for i in topic_li:
        Topic.objects.create(topic=i)
# create_topics()

def create_people_cards():
    for data in people:
        PeopleCard.objects.create(name=data['name'], height=data['height'], home_world=requests.get(data['homeworld']).json()['name'], mass=data['mass'])

# create_people_cards()

def create_vehicle_cards():
    for data in vehicles:
        VehicleCard.objects.create(name=data['name'], model=data['model'], vehicle_class=data['vehicle_class'], max_atmosphering_speed=data['max_atmosphering_speed'])

# create_vehicle_cards()
# class PeopleCard(models.Model):
#     name = models.CharField(max_length=50)
#     height  = models.CharField(max_length=50)
#     homeworld = models.CharField(max_length=50)
#     mass = models.CharField(max_length=50)

# class VehicleCard(models.Model):
#     name = models.CharField(max_length=50)
#     model   = models.CharField(max_length=50)
#     vehicle_class  = models.CharField(max_length=50)
#     max_atmosphering_speed = models.CharField(max_length=50)