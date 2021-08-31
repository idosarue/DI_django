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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     senders = Transaction.objects.all().values_list('trade_sender_id', flat=True)
    #     senders2 = TransactionResponse.objects.all().values_list('trade_sender_id', flat=True)
    #     for sender_id in senders:
    #         context['trade_sender'] = Profile.objects.get(id=sender_id)
    #     print(context)
    #     return context

class TradeDetailView(DetailView):
    model = Transaction
    template_name = 'trading/trade_details.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['response_transaction'] = TransactionResponse.objects.all()
    #     return context

class TradeResponseView(CreateView):
    form_class = TransactionResponseForm
    template_name = 'trading/trade_response.html'
    success_url = reverse_lazy('home')

    def get_trade(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Transaction, id=thread_id)

    def form_valid(self, form): 
        transaction_response = form.save(commit=False)
        original_transaction = self.get_trade()
        trade_obj = self.get_trade().trade_sender_id
        transaction_response.trade_reciever = Profile.objects.get(id=trade_obj)
        original_transaction.trade_reciever = self.request.user.profile
        # original_transaction.trade_sender = Profile.objects.get(id=trade_obj)
        print(original_transaction.trade_reciever, 'orig')
        print(transaction_response.trade_reciever, 'res')

        transaction_response.trade_sender = self.request.user.profile
        transaction_response.original_transaction = self.get_trade()
        transaction_response.save()
        original_transaction.save()
        print(transaction_response)
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form


def update_trade_status(request, pk, status):
    transaction = get_object_or_404(Transaction, id=pk)

    if status == 'accept':
        transaction.trade_choice = 1

        transaction.save()
        return redirect('trade_response_back', pk)
    else:
        transaction.trade_choice = 0
    transaction.save()
    return redirect('home')

def update_trade_back_status(request, pk, status):
    transaction_re = get_object_or_404(TransactionResponse, id=pk)
    print(transaction_re)
    if status == 'accept':
        transaction_re.trade_choice = 1 
        if transaction_re.swap_cards():
            user1_re = transaction_re.original_transaction.trade_reciever
            user2_re = transaction_re
            user1 = Profile.objects.get(id=user1_re.id)
            print(user1, 'user1')
            user2 = Profile.objects.get(id=user2_re.trade_reciever.id)
            print(user2, 'user2')
            card1 = transaction_re.original_transaction.card
            print(card1, 'card1')
            card2 = transaction_re.card
            print(card2, 'card2')

            user1.deck.remove(card2)
            user1.deck.add(card1) 
            user2.deck.remove(card1)
            user2.deck.add(card2)
            print(user1.deck.all())
            print(user2.deck.all())
            transaction_re.save()
    else:
        transaction_re.trade_choice = 0
    transaction_re.save()
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