from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignupForm
from django.views.generic import CreateView
# Create your views here.

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
