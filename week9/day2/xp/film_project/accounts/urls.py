from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserCreationView.as_view(),name='signup'),
    path('login', views.UserLoginView.as_view(),name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<int:pk>', views.UserDetailView.as_view(), name='profile'),
]