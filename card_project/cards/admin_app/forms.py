from django import forms
from .models import Store
from django.contrib.auth.models import User
from trading.models import Card

class StoreTransactionForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        