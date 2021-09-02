from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.TransactionListView.as_view(), name='home'),
    path('create_trade/', views.CreateTradeView.as_view(), name='create_trade'),
    path('trade_response/<int:pk>/<str:status>/', views.update_trade_status, name='trade_response'),
    path('trade_response_status/<int:pk>/<str:status>/', views.update_trade_back_status, name='trade_response_status'),
    path('trade_response/<int:pk>/', views.TradeResponseView.as_view(), name='trade_response_back'),
    path('trade_details/<int:pk>/', views.TradeDetailView.as_view(), name='trade_details'),
    path('store', views.StoreView.as_view(), name='store'),
    path('card_details/<int:pk>/', views.CardDetailView.as_view(), name='card_details'),
    path('offer_sale/', views.SellCardView.as_view(), name='offer_sale'),
    path('card_sales/', views.SellTransactionListView.as_view(), name='card_sales'),
    path('sell_card/<int:pk>/', views.sell_card_to_store, name='sell_card'),
    path('offer_card_status/<int:pk>/<str:status>/', views.buy_card, name='offer_card_status'),
    path('offer_card_status/<int:pk>/', views.buy_card_from_store, name='buy_card_from_store'),
    path('get_user_to_sell/<int:pk>/', views.get_user_to_sell, name='get_user_to_sell'),
]