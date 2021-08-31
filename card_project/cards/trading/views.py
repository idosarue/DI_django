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
    # def get_reciever(self):
    #     thread_id = self.kwargs['pk']
    #     return get_object_or_404(Profile, id=thread_id)


    # def form_valid(self, form): 
    #     transaction = form.save(commit=False)
    #     transaction.trade_reciever = transaction
    #     transaction.trade_sender = self.request.user.profile
    #     transaction.save()
    #     return super().form_valid(form)


    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     form.fields['card'].queryset = self.request.user.profile.deck.all()
    #     return form

class TradeResponseView(CreateView):
    form_class = TransactionResponseForm
    template_name = 'trading/trade_response.html'
    success_url = reverse_lazy('home')

    def get_trade(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Transaction, id=thread_id)

    def form_valid(self, form): 
        transaction_response = form.save(commit=False)
        trade_obj = self.get_trade().trade_sender_id
        original_transaction = self.get_trade()
        original_transaction.trade_reciever = Profile.objects.get(id=trade_obj)
        original_transaction.trade_sender = self.request.user.profile
        transaction_response.trade_reciever = Profile.objects.get(id=trade_obj)
        transaction_response.trade_sender = self.request.user.profile
        transaction_response.save()
        original_transaction.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        senders = Transaction.objects.all().values_list('trade_sender_id', flat=True)
        for sender_id in senders:
            context['trade_reciever'] = Profile.objects.get(id=sender_id)
        return context

def update_trade_status(request, pk, status):
    f = get_object_or_404(Transaction, id=pk)
    if status == 'accept':
        f.trade_choice = 1
        f.save()
        return redirect('trade_response_back', pk)
    else:
        f.trade_choice = 0
    f.trade_reciever = request.user.profile
    f.save()
    return redirect('home')

class CreateTradeView(CreateView):
    form_class = TransactionForm
    template_name = 'trading/create_trade.html'
    success_url = reverse_lazy('home')

    def get_trade(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Transaction, id=thread_id)


    # def form_valid(self, form): 
    #     transaction = form.save(commit=False)
    #     transaction.trade_sender = self.request.user.profile
    #     transaction.save()
    #     return super().form_valid(form)

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