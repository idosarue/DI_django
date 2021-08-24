from django.urls import path
from . import views
urlpatterns = [
    path('homepage', views.FilmListView.as_view(), name='home'),
    path('add_film', views.AddFilm.as_view(), name='add_film'),
    path('add_comment/<int:id>', views.AddCommentRate.as_view(), name='add_comment'),
    path('add_director', views.add_director, name='add_director'),
    path('delete_film/<int:id>', views.delete_film, name='delete_film'),
    path('delete_director/<int:id>', views.delete_director, name='delete_director'),
]
