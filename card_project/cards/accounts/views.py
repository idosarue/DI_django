
from accounts.models import Profile, Topic
from trading.models import Card
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ProfileForm, SignupForm
from django.views.generic import CreateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(self.request, username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'] )   
        if user:
            profile_form = ProfileForm(self.request.POST)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                messages.error(self.request, 'Something went wrong')
            login(self.request, user)
        else:
            messages.error(self.request, 'Something went wrong')
        return redirect('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = Card.objects.filter(owners= self.request.user.profile.id)
        return context