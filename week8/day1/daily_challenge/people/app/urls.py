from django.urls import path
from .views import home, people

urlpatterns = [
    path('', home),
    path('/<int:num>', people, name='people'),
    # "/people/people{id}"

]
