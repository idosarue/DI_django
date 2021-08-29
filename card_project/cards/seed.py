import os
import django
import json
import requests



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cards.settings')
django.setup()
response = requests.get('https://pokeapi.co/api/v2/')
print(response.text)