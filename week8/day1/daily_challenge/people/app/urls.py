from django.urls import path
from .views import home, people

urlpatterns = [
    path('people', home),
    path('people/people/<int:num>', people, name='people'),

]
