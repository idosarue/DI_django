from django import forms
from .models import Transaction, TransactionResponse
from django.contrib.auth.models import User
from trading.models import Card

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['card']
        
class TransactionResponseForm(forms.ModelForm):
    class Meta:
        model = TransactionResponse
        fields = ['card']
        
# class CardBuyForm(forms.ModelForm):
#     class Meta:
#         model = Card
#         fields = ['card']
