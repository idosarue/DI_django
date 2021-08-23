from django.urls import path
from . import views
urlpatterns = [
    path('homepage', views.FilmListView.as_view(), name='home'),
    path('add_film', views.AddFilm.as_view(), name='add_film'),
    path('add_director', views.add_director, name='add_director'),
]
