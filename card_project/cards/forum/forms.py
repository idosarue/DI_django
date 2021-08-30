from django import forms
from django.forms import fields
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['subject']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']