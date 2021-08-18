from django.shortcuts import redirect, render, HttpResponse
from phonenumber_field.modelfields import PhoneNumberField
from .models import Person
import re
from .forms import AddPersonForm, SearchPersonForm
from django.http import HttpResponseRedirect
# Create your views here.

# 1	john	john@gmail.com	+12125552368	tel aviv
# 2	jane	jane@gmail.com	+13145552367	tel aviv


def add_person(request):
    if request.method == 'GET':
        form = AddPersonForm()
    elif request.method == 'POST':
        form = AddPersonForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Person.objects.create(**form.cleaned_data)
            return redirect('search-person')
    return render(request, 'add_person.html', {'form':form})



def search_person(request):
    if request.method == 'GET':
        form = SearchPersonForm()
    elif request.method == 'POST':
        form = SearchPersonForm(request.POST)
        if form.is_valid():
            phone_num = form.cleaned_data['phone_number']
            name = form.cleaned_data['name']

            if phone_num:
                return redirect('phone_number', phone_num)
            elif name:
                # f = Person.objects.filter(name = name)
                return redirect('name', name)
    return render(request, 'search.html', {'form':form})


        
def phone_number(request ,phone_num):
    f = Person.objects.filter(phone_number = phone_num)
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