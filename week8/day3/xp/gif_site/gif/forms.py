
from django.forms import ModelForm, models
from .models import Category, Gif


class GifForm(ModelForm):
    class Meta:
        model = Gif
        exclude = ('likes',)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

class likeForm(ModelForm):
    class Meta:
        model = Gif
        fields = ('likes', )