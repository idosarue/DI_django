from django.urls import path
from . import views
urlpatterns = [
    path('rental', views.rent, name='rental'),
    path('rental/<int:pk>', views.display_rental_details, name='get_data'),
    path('rental_details/<int:pk>', views.rental_details, name='rental_details'),
    path('rental/add', views.add_rental, name='add_rental'),
    path('customer/<int:pk>', views.show_customer, name='show_customer'),
    path('customers', views.show_customers, name='show_customers'),
    path('add_customer', views.add_customer, name='add_customers'),
    path('vehicles', views.show_vehicles, name='show_vehicles'),
    path('vehicle/<int:pk>', views.show_vehicle, name='show_vehicle'),
    path('add_vehicle', views.add_vehicle, name='add_vehicle'),
]
