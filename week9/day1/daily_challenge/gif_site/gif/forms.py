
from django.forms import ModelForm, models
from .models import Category, Gif
from django.utils.translation import gettext_lazy as _
# class Gif(models.Model):
#     title = models.CharField(max_length=80)
#     url = models.URLField(unique=True)
#     uploader_name = models.CharField(max_length=50)
#     categories = models.CharField(max_length=20,choices=DEMO_CHOICES, default='asd')
#     created_at = models.DateTimeField(auto_now_add=True)

class GifForm(ModelForm):
    class Meta:
        model = Gif
        exclude = ('likes',)
        labels = {
        'name': _('Title'),
        'url': _('URl'),
        'uploader_name': _('your name'),

        }



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

class likeForm(ModelForm):
    class Meta:
        model = Gif
        fields = ('likes', )
