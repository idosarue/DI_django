from django.shortcuts import render, HttpResponse
import json
from django.contrib import  messages
from django.contrib.messages import get_messages

# Create your views here.

with open("animals.json", "r") as f :
    x = json.load(f)


MESSAGE_TAGS = {
    messages.INFO: '',
}

def family(request, num):
    animal_li= []
    if num > len(x['families']) or not num:
        return HttpResponse('Error')
    else:
        for item in x['animals']:
            if item['family'] == num:
                animal_li.append(item['name'])
        context = {
            'animals' : animal_li,
        }

        return render(request, 'index.html', context)

def animal(request, num):
    info_li= []
    if num > len(x['animals']) or not num:
        return HttpResponse('Error')
    else:
        for item in x['animals']:
            if item['id'] == num:
                for key, value in item.items():
                    if key != 'id':
                        info_li.append(f'{key} : {value}')
        context = {
            'animals' : info_li,
        }

        return render(request, 'index.html', context)

