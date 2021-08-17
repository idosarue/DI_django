from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import  CategoryForm, GifForm, likeForm
from .models import Gif, Category

def home(request):
    f = Gif.objects.values_list('url', flat=True)
    return render(request, 'home.html', {'images' : f})

def add_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_gif.html', {'form' : form})
    else:
        form = GifForm()
    return render(request, 'add_gif.html', {'form' : form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request, 'add_gif.html', {'form' : form})
    else:
        form = CategoryForm()
    return render(request, 'add_gif.html', {'form' : form})    

def category(request, category_id):
    f = Gif.objects.filter(categories=category_id).values_list('url',flat=True)
    if not f:
        return HttpResponse('no gifs in category')
    return render(request, 'category.html', {'category' : f}) 


def gif(request, gif_id):
    f = Gif.objects.filter(id=gif_id).values_list('url',flat=True)
    if not f:
        return HttpResponse('gif does not exist')
    return render(request, 'gif.html', {'gifs' : f}) 

def categories(request):
    f = Category.objects.all()
    print(f)
    return render(request, 'categories.html', {'categories' : f})


def like(request):
    # f = Gif.objects.()

    # if the submit button was clicked
    if request.method == 'POST':
        # POST, generate form with data from the request
        
        form = likeForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            like_li = []
            print(form)
            like = form.cleaned_data['likes']
            return render(request, 'likes.html')
    else:
        # GET, generate blank form
        form = likeForm()
    return render(request, 'likes.html', {'form' : form})