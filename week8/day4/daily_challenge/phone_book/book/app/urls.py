from django.urls import path
from . import views

urlpatterns = [
    path('persons/phonenumber/<str:phone_num>', views.phone_number, name='phone_number'),
    path('persons/name/<str:name>', views.name, name='name'),
    path('add_person', views.add_person, name='add_person'),
    path('search', views.search_person, name='search_person'),

]
