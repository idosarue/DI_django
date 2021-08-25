from django.db import models
from django.forms import fields
from .models import Image
from django import forms

class ImgForm(forms.ModelForm):
    class Meta:
        model= Image
        fields='__all__'
        
class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()