# from film_project import films
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

class FilmListView(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = 'films' 
    model = Film


class AddFilm(generic.CreateView):
    form_class = AddFilmForm
    template_name = 'film/add_film.html'
    success_url = reverse_lazy('add_director')


def add_director(request):
    if request.method == 'GET':
        form = AddDirectorForm()
    elif request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            films = form.cleaned_data['film']
            # director_first = form.cleaned_data['first_name']
            # director_last = form.cleaned_data['last_name']
            # director = Director.objects.get(first_name__icontains=director_first, last_name__icontains=director_last)
            # for i in film_name:
            director = form.save()

            director.film_set.add(*films)
            return redirect('home')
    return render(request, 'director/add_director.html', {'form' : form})


# class AddDirector(generic.CreateView):
#     form_class = AddDirectorForm
#     template_name = 'director/add_director.html'
#     success_url = reverse_lazy('home')

