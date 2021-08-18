from django import forms
from django.db import models
from .models import Category, Todo


class TodoForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=40)
    details = forms.CharField(max_length=40)
    deadline_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    