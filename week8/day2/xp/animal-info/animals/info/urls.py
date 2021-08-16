from info.models import Family
from django.urls import path
from .views import family, animal, animals


urlpatterns = [
    path('family/<int:family_id>', family),
    path('animal/<int:animal_id>', animal),
    path('animals/', animals, name='animal'),

]
