from accounts.forms import RegisterForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from django.contrib.auth import authenticate, login
from .models import NewUser, Profile
from django.contrib.auth import logout

# Create your views here.
    # path('signup', views.UserCreationView,name='signup'),
    # path('login', views.UserLoginView,name='login'),
    # path('logout', views.logout, name='logout'),
    # path('profile', views.profile, name='ptofile'),

class UserCreationView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        Profile.objects.create(user=user)
        
        user.save()
        print(form.cleaned_data) 
        user = authenticate(self.request,email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        print(user)
        if user:
            login(self.request, user)
            print('logged in')
            return redirect('home')
        else:
            print('asd')
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class UserLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

class UserDetailView(DetailView):
    template_name = 'profile.html'
    model = Profile

def logout_view(request):
    logout(request)
    return redirect('login')