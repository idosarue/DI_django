# from film_project import films
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

@login_required
def delete_film(request, id):
    if request.user.is_superuser:
        f = get_object_or_404(Film, id=id)
        # f.director.clear()
        f.delete()
        messages.success(request, 'film deleted.')

    return redirect('home') 

@login_required
def delete_director(request, id):
    if request.user.is_superuser:
        f = get_object_or_404(Director, id=id)
        f.delete()
        messages.success(request, 'director deleted.')
    return redirect('home') 

class AddCommentRate(generic.UpdateView):
    form_class = CommentRateForm
    template_name = 'film/add_comment.html'
    success_url = reverse_lazy('home')
    queryset = Film.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Film, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# class RateMovie(generic.UpdateView):
#     form_class = RateMovieForm
#     template_name = 'film/add_comment.html'
#     success_url = reverse_lazy('home')
#     queryset = Film.objects.all()

#     def get_object(self):
#         id = self.kwargs.get("id")
#         return get_object_or_404(Film, id=id)

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
