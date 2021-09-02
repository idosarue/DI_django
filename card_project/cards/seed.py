import os
import django
import json
import requests
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cards.settings')
django.setup()

from accounts.models import Topic
from trading.models import PeopleCard, VehicleCard, Card
from admin_app.models import Store

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
        PeopleCard.objects.create(name=data['name'], height=data['height'], home_world=requests.get(data['homeworld']).json()['name'], mass=data['mass'], c_type="P")

# create_people_cards()

def create_vehicle_cards():
    for data in vehicles:
        VehicleCard.objects.create(name=data['name'], model=data['model'], vehicle_class=data['vehicle_class'], max_atmosphering_speed=data['max_atmosphering_speed'], c_type="V")


# create_vehicle_cards()


def create_rarity():
    vehicle_cards = VehicleCard.objects.all().order_by('max_atmosphering_speed')
    people_cards = PeopleCard.objects.all().order_by('name')
    counter = 0
    for i in vehicle_cards:
        counter+=1
        print(i.max_atmosphering_speed)
        i.rarity = counter
        i.save()
    new_counter = 0
    for x in people_cards:
        new_counter+=1
        x.rarity = new_counter
        x.save()

# create_rarity()

def add_to_store():
    for i in Card.objects.all():
        Store.objects.create(cards=i)
    
# add_to_store()

