from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.TransactionListView.as_view(), name='home'),
    path('create_trade/', views.CreateTradeView.as_view(), name='create_trade'),
    path('trade_response/<int:pk>/<str:status>/', views.update_trade_status, name='trade_response'),
    path('trade_response/<int:pk>/', views.TradeResponseView.as_view(), name='trade_response_back'),
    path('trade_details/<int:pk>/', views.TradeDetailView.as_view(), name='trade_details'),
]
