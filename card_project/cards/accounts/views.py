
from accounts.models import Profile, Topic
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ProfileForm, SignupForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        user = authenticate(self.request, username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'] )   
        if user:
            login(self.request, user)
        else:
            messages.error(self.request, 'Something went wrong')
        return redirect('home')
    
