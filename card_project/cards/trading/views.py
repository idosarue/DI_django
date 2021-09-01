from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TransactionForm, TransactionResponseForm
from .models import Card, Transaction, TransactionResponse
from accounts.models import Profile

class TransactionListView(ListView):
    model = Transaction
    template_name = 'trading/home.html'

class TradeDetailView(DetailView):
    model = Transaction
    template_name = 'trading/trade_details.html'

class TradeResponseView(CreateView):
    form_class = TransactionResponseForm
    template_name = 'trading/trade_response.html'
    success_url = reverse_lazy('home')

    def get_trade(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Transaction, id=thread_id)

    def form_valid(self, form): 
        transaction_response = form.save(commit=False)
        transaction_response.trade_sender = self.request.user.profile
        transaction_response.original_transaction = self.get_trade()
        transaction_response.save()
        print(transaction_response)
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trade_sender'] = self.get_trade().trade_sender
        return context



def update_trade_status(request, pk, status):
    transaction = get_object_or_404(Transaction, id=pk)
    card = transaction.card
    if status == 'accept':
        transaction.trade_choice = 1
        transaction.trade_reciever = request.user.profile
        if not transaction.trade_reciever.deck.filter(id = Card.objects.get(id=card.id).id).exists():
            transaction.save()
            return redirect('trade_response_back', pk)
        else:
            transaction.trade_choice = 0
            transaction.save()
            messages.error(request, 'You already have that card, you can\'t have duplicates trade rejected')
            return redirect('home')

    else:
        transaction.trade_choice = 0
        transaction.save()
        return redirect('home')

def update_trade_back_status(request, pk, status):
    transaction = get_object_or_404(TransactionResponse, id=pk)
    first_trans = transaction.original_transaction
    second_trans = transaction
    user1 = Profile.objects.get(id=first_trans.trade_sender.id)
    user2 = Profile.objects.get(id=second_trans.original_transaction.trade_reciever.id)
    card1 = first_trans.card
    card2 = second_trans.card
    if status == 'accept':
        if not user1.deck.filter(id = Card.objects.get(id=card2.id).id).exists():
            transaction.trade_choice = 1 
            if transaction.swap_cards():
                print(user1, 'user1')
                print(user2, 'user2')
                print(first_trans.card, 'first_trans.card')
                print(second_trans.card, 'secontrans.card')
                print(card1, 'card1')
                print(card2, 'card2')
                user1.deck.add(card2) 
                user1.deck.remove(card1) 
                user2.deck.add(card2)
                user2.deck.remove(card1)
                transaction.save()
                messages.success(request, 'trade was succesfull!')
                return redirect('home')
        else:
            transaction.trade_choice = 0
            transaction.save()
            messages.error(request, 'You already have that card, you can\'t have duplicates. trade rejected')
            return redirect('home')
    else:
        transaction.trade_choice = 0
        transaction.save()
    return redirect('home')



class CreateTradeView(CreateView):
    form_class = TransactionForm
    template_name = 'trading/create_trade.html'
    success_url = reverse_lazy('home')

    def get_trade(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Transaction, id=thread_id)

    def form_valid(self, form): 
        transaction = form.save(commit=False)
        transaction.trade_sender = self.request.user.profile
        transaction.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = self.request.user.profile.deck.all()
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form