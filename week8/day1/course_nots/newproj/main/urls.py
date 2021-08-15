
from django.urls import path
from .views import homepage,about,home,calc


urlpatterns = [
    path('', homepage),
    path('about', about),
    path('index', home),
    path('calc/<int:num>', calc),
    path('nocalc/', calc)

]


