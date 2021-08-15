from django.urls import path
from .views import family, animal

urlpatterns = [
    path('family/<int:num>', family),
    path('animal/<int:num>', animal)
]
