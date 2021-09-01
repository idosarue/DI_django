from admin_app.models import Store
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from trading.models import Card
from django.contrib.auth.decorators import login_required
from .forms import CreateCardForm
# Create your views here.
def home(request):
    return render(request, 'trading/home.html')

class CreateCardView(LoginRequiredMixin, CreateView):
    form_class = CreateCardForm
    template_name = 'admin/add_card.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        messages.success(self.request, 'Added Card')
        return super().form_valid(form)