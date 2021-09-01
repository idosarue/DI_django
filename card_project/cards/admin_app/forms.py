from django import forms
from .models import Store
from django.contrib.auth.models import User
from trading.models import Card

class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['owners']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Card.objects.filter(name=name).exists():
            raise forms.ValidationError('Card with that name already exists.')
        print(name)
        return name