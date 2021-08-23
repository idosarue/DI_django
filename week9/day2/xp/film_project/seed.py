
import os
import django
from faker import Faker


fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'film_project.settings')
django.setup()
from films.models import *


def create_countries(num):
    for _ in range(num):
        country = fake.country()
        return country

def generate_categories():
    categories = ["Action",
    "Comedy",
    "Drama",
    "Fantasy",
    "Horror",
    "Mystery",
    "Romance",
    "Thriller"]
    for i in categories:
        Category.objects.create(name=i)

# generate_categories()

def generate_countries(num):
    for _ in range(num):
        country = create_countries(num)
        Country.objects.create(name=country)

# generate_countries(10)