import os
import django
import json
import requests



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cards.settings')
django.setup()

from accounts.models import Topic

response_people = requests.get('https://swapi.dev/api/people')
response_vehicles = requests.get("https://swapi.dev/api/vehicles/")


people = response_people.json()['results']
vehicles = response_vehicles.json()['results']

for i in people:
    print(i['name'])

for i in vehicles:
    print(i['name'])



def create_topics():
    topic_li = ['Wookie', 'Hutt', 'Jedi', 'StormTrooper(not recommended)']
    for i in topic_li:
        Topic.objects.create(topic=i)

# create_topics()