from trading.models import Transaction
from admin_app.models import Store
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import CreateCardForm
from forum.models import Thread
from django.contrib.auth.decorators import user_passes_test

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class CreateCardView(SuperUserRequiredMixin, CreateView):
    form_class = CreateCardForm
    template_name = 'admin/add_card.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        card = form.save()
        store = Store.objects.create(store_card=card)
        store.save()
        print(store)
        return super().form_valid(form)
        
@user_passes_test(lambda u: u.is_superuser)
def delete_card_from_store(request, pk):
    card = get_object_or_404(Store, id=pk)
    print(card.quantity, 'fs')
    card.quantity -= 1
    card.store_card.quantity -=1
    print(card.quantity)
    print(card.store_card.quantity)
    card.save()
    card.store_card.save()
    messages.success(request, 'Card deleted')
    return redirect('store')

@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, pk):
    thread = get_object_or_404(Thread, id=pk)
    thread.delete()
    messages.success(request, 'thread deleted')
    return redirect('all_threads')

@user_passes_test(lambda u: u.is_superuser)
def delete_trade(request, pk):
    trade = get_object_or_404(Transaction, id=pk)
    trade.delete()
    messages.success(request, 'trade deleted')
    return redirect('home')

