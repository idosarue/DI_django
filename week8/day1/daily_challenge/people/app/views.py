from django.shortcuts import render, HttpResponse
import json

with open('people.json', 'r') as f:
    x = json.load(f)

def home(request):
    people_li = []

    for item in x['people']:
        people_li.append(item)

    context = {
        'people' : sorted(people_li, key=lambda x: x['age'])
    }
    return render(request, 'home.html', context)

def people(request, num):
    people_li= []
    if num > len(x['people']) or not num:
        return HttpResponse('Error')
    else:
        for item in x['people']:
            if item['id'] == num:
                people_li.append(item) 
                # for key, value in item.items(): 
                #     people_li.append(f'{key} : {value}') another way
        print(people_li)
        context = {
            'person' : people_li,
        }
    return render(request, 'people.html', context)
