from django.urls import path
from .import views

urlpatterns = [
    path('create_card/', views.CreateCardView.as_view(), name = 'create_card'),
    path('delete_card/<int:pk>/', views.delete_card_from_store, name = 'delete_card'),
]
