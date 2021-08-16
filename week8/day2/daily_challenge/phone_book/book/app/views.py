from django.shortcuts import render, HttpResponse
from .models import Person
import re
from .forms import PersonForm
from django.http import HttpResponseRedirect
# Create your views here.

# 1	john	john@gmail.com	+12125552368	tel aviv
# 2	jane	jane@gmail.com	+13145552367	tel aviv


def add_person(request):
    submitted = False
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_person?submitted=True')
    else:
        form = PersonForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'add_person.html', {'form' : form, 'submitted' : submitted})

        
def phone_number(request ,phone_num):
    f = Person.objects.filter(phoneNumber = phone_num)
    if not f or re.search('[a-zA-Z]', phone_num):
        return HttpResponse('invalid')
    else:
        return render(request, 'info.html', {"person" : f})
def name(request ,name):
    f = Person.objects.filter(name = name)
    if not f:
        return HttpResponse('name  does not exist')
    else:
        return render(request, 'info.html', {"person" : f})