from admin_app.models import Store
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from trading.models import Card
from django.contrib.auth.decorators import login_required
from .forms import CreateCardForm
from forum.models import Thread

# Create your views here.
def home(request):
    return render(request, 'trading/home.html')

class CreateCardView(LoginRequiredMixin, CreateView):
    form_class = CreateCardForm
    template_name = 'admin/add_card.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        card = form.save()
        store = Store.objects.create(cards=card)
        print(store)
        return super().form_valid(form)
@login_required
def delete_card_from_store(request, pk):
    if request.user.is_superuser:
        store_card = get_object_or_404(Store, cards_id=pk)
        print(store_card.quantity, 'fs')
        store_card.quantity -= 1
        store_card.save()
        messages.success(request, 'Card deleted')
    return redirect('store')

def delete_post(request, pk):
    if request.user.is_superuser:
        thread = get_object_or_404(Thread, id=pk)
        thread.delete()
        messages.success(request, 'thread deleted')
    return redirect('all_threads')

