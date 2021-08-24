from django import forms
from django.db.models.query_utils import Q
from django.forms import ModelForm, fields
from .models import Film, Director
from django.forms import modelformset_factory

class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        exclude = ('director', 'comment',)

class AddDirectorForm(ModelForm):
    film = forms.ModelMultipleChoiceField(queryset=Film.objects.all())
    class Meta:
        model = Director
        fields = '__all__'

class CommentRateForm(ModelForm):
    class Meta:
        model = Film
        fields = ('comment', 'rating',)

# class RateMovieForm(ModelForm):
#     class Meta:
#         model = Film
#         fields = (, )

# AnimalFormSet = modelformset_factory(Film, form=CommentRateForm, extra=0)
