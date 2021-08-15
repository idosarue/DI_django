from django.shortcuts import render, HttpResponse

# Create your views here.
# def homepage(request):
#     return HttpResponse('Hello world')


def about(request):
    return HttpResponse('about page')


def home(request):
    return render(request,'index.html')


def homepage(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'index.html', context)

def calc(request, num=100):

    context = {
        'div' : num/10,
        'mult' : num *10,
        'add' : num + 10
    }


    return render(request, 'calc.html', context)