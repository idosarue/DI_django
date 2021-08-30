from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.TransactionListView.as_view(), name='home'),
    path('create_trade/', views.CreateTradeView.as_view(), name='create_trade'),
]
