from accounts.models import Profile
from django import forms
from django.forms import fields
from .models import Card, Transaction
from django.contrib.auth.models import User

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['trade_reciever']

    

