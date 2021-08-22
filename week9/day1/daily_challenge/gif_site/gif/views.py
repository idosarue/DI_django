from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
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
    # f = Gif.objects.filter(id=gif_id).values_list('url',flat=True)
    f = get_object_or_404(Gif, id=gif_id)
    return render(request, 'gif.html', {'gifs' : f}) 

def categories(request):
    f = Category.objects.all()
    print(f)
    return render(request, 'categories.html', {'categories' : f})


def like(id):
    f = get_object_or_404(Gif, id=id)
    # if the submit button was clicked
    f.likes +=1
    f.save()
    return redirect('gifs', id)

def dislike( id):
    f = get_object_or_404(Gif, id=id)
    # if the submit button was clicked
    f.likes -=1
    f.save()
    return redirect('gifs', id)