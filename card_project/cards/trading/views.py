from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def home(request):
    return render(request, 'trading/home.html')