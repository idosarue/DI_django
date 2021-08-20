from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_gif', views.add_gif, name='gif'),
    path('add_categories', views.add_category, name='categories'),
    path('category/<int:category_id>', views.category, name='category'),
    path('gif/<int:gif_id>', views.gif, name='gifs'),
    path('categories', views.categories, name='all_categories'),
    path('likes/<int:id>', views.like, name='likes'),
    path('dislikes/<int:id>', views.dislike, name='dislikes'),

]
