from django.urls import path
from . import views

urlpatterns = [
    path('balance/', views.get_wallet_balance, name='get_wallet_balance'),
    path('add/', views.add_balance, name='add_balance'),    
    path('transfer/', views.transfer_balance, name='transfer_balance'),
    path('transactions/', views.list_transactions, name='list_transactions'),
]
