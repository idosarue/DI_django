from django.urls import path
from . import views

urlpatterns = [
    path('persons/phonenumber/<str:phone_num>', views.phone_number),
    path('persons/name/<str:name>', views.name),
    path('add_person', views.add_person, name='add-person'),
]
