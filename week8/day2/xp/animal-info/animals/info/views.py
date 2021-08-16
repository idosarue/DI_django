from django.shortcuts import render, HttpResponse
from .models import Family, Animal

def family(request,family_id):
    f = Animal.objects.filter(family_id=family_id)
    return render(request, 'family.html', {'family' : f})

def animal(request, animal_id):
    a = Animal.objects.filter(id=animal_id)
    return render(request, 'animal.html', {'animals' : a})

def animals(request):
    a = Animal.objects.all()
    return render(request, 'animals.html', {'animals' : a})
