from django import forms
from django.db.models.query_utils import Q
from django.forms import ModelForm, fields
from .models import Film, Director

class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        exclude = ('director', )

class AddDirectorForm(ModelForm):
    film = forms.ModelMultipleChoiceField(queryset=Film.objects.all())
    class Meta:
        model = Director
        fields = '__all__'

