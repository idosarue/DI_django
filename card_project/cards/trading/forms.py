from django import forms
from .models import Transaction, TransactionResponse
from django.contrib.auth.models import User

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['card']


class TransactionResponseForm(forms.ModelForm):
    class Meta:
        model = TransactionResponse
        fields = ['card']

    