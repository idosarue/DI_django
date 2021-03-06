from admin_app.models import Store
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import TransactionForm, TransactionResponseForm, SellCardTransactionForm
from .models import Card, Transaction, TransactionResponse, SellCardTransaction
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django import forms

class TransactionListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'trading/home.html'

class TradeDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'trading/trade_details.html'

class TradeResponseView(LoginRequiredMixin, CreateView):
    form_class = TransactionResponseForm
    template_name = 'trading/trade_response.html'
    success_url = reverse_lazy('home')

    def get_trade(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Transaction, id=thread_id)

    def form_valid(self, form): 
        transaction_response = form.save(commit=False)
        transaction_response.original_transaction = self.get_trade()
        transaction_response.save()
        print(transaction_response)
        return super().form_valid(form)

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        original_transaction = self.get_trade()
        sender = original_transaction.trade_sender.deck.all()
        reciever = original_transaction.trade_reciever.deck.all()
        dif = list(set(reciever) - set(sender))
        context['trade_options'] = dif # get the options for trade for user
        context['trade_sender'] = self.get_trade().trade_sender
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form
    
@login_required
def update_trade_status(request, pk, status):
    transaction = get_object_or_404(Transaction, id=pk)
    card = transaction.card
    user = Profile.objects.get(id=transaction.trade_sender.id)
    if status == 'accept':
        transaction.trade_choice = 1
        transaction.trade_reciever = request.user.profile
        if not transaction.trade_reciever.deck.filter(id = Card.objects.get(id=card.id).id).exists(): 
            transaction.choice = 'A'
            transaction.save()
            return redirect('trade_response_back', pk)
        else:
            transaction.trade_choice = 0
            transaction.save()
            messages.error(request, 'You already have that card, you can\'t have duplicates trade rejected')
            return redirect('home')

    else:
        user.score -= 5
        user.save()
        transaction.trade_choice = 0
        transaction.save()
        return redirect('home')

@login_required
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
            print(transaction.original_transaction.choice)
            if transaction.swap_cards():
                print(user1, 'user1')
                print(user2, 'user2')
                print(first_trans.card, 'first_trans.card')
                print(second_trans.card, 'secontrans.card')
                print(card1, 'card1')
                print(card2, 'card2')
                print(user1.deck.all(), 'before1')
                print(user2.deck.all(), 'before2')
                user1.deck.add(card2) 
                user1.deck.remove(card1) 
                user2.deck.add(card1)
                user2.deck.remove(card2)
                transaction.save()
                user1.coins += 10
                user2.coins += 10
                user1.score += 10
                user2.score += 10
                user1.save()
                user2.save()
                print(user1.deck.all(), 'after1')
                print(user2.deck.all(), 'after2')
                messages.success(request, 'trade was succesfull! score+10 coins+10')
                return redirect('home')
        else:
            user1.score -= 5
            user2.score -= 5
            user1.save()
            user2.save()
            transaction.trade_choice = 0
            transaction.save()
            messages.error(request, 'You already have that card, you can\'t have duplicates. trade rejected -5 points')
            return redirect('home')
    else:
        user1.score -= 5
        user1.save()
        print('asd')
        transaction.trade_choice = 0
        transaction.save()
    return redirect('home')



class CreateTradeView(LoginRequiredMixin, CreateView):
    form_class = TransactionForm
    template_name = 'trading/create_trade.html'
    success_url = reverse_lazy('home')

    

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


class StoreView(LoginRequiredMixin, ListView):
    model = Store
    template_name = 'trading/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards_li = [card for card in Store.objects.all() if card.quantity > 0]
        context['cards'] = cards_li
        return context

class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = 'trading/card_details.html'
    success_url = reverse_lazy('home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form



def sell_card_to_store(request, pk):
    card = get_object_or_404(Card, id=pk)
    user = request.user.profile
    user_deck = user.deck
    if len(user_deck.all()) > 12:
        user_deck.remove(card)
        user.coins += card.price - (card.price / 10)
        user.save()
        messages.success(request, 'Card sold.')
    else:
        messages.error(request, 'You can\'t have less than 12 cards.')
    
    return redirect('profile')

#  BuyCardResponseForm, SellCardTransactionForm

def get_user_to_sell(request, pk):
    user = get_object_or_404(Profile, id=pk)
    print(user.is_seller_deck_valid())
    if user.is_seller_deck_valid():
        return redirect('offer_sale')
    else:
        messages.error(request, 'you can\'t sell if you have 12 or less cards')
        return redirect('profile')



class UserDeckRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.profile.is_seller_deck_valid()

class SellCardView(UserDeckRequiredMixin, CreateView):
    form_class = SellCardTransactionForm
    template_name = 'trading/sell_card.html'
    success_url = reverse_lazy('card_sales')

    def form_valid(self, form): 
        transaction = form.save(commit=False)
        transaction.seller = self.request.user.profile
        transaction.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.all()
        return form


class SellTransactionListView(LoginRequiredMixin,ListView):
    model = SellCardTransaction
    template_name = 'trading/selling.html'


@login_required
def buy_card(request, pk, status):
    transaction = get_object_or_404(SellCardTransaction, id=pk)
    card = transaction.card
    seller = Profile.objects.get(id=transaction.seller.id)
    if status == 'accept':
        transaction.trade_choice = 1
        transaction.buyer = request.user.profile
        if len(transaction.buyer.deck.all()) <= 14:
            if not transaction.buyer.deck.filter(id = Card.objects.get(id=card.id).id).exists():
                if transaction.buyer.coins >= card.price:
                    seller.deck.remove(card)
                    seller.coins += card.price
                    transaction.buyer.coins -= card.price
                    transaction.buyer.deck.add(card)
                    print(seller, 'seller')
                    print(transaction.buyer, 'buyer')
                    print(card.price)
                    seller.save()
                    transaction.buyer.save()
                    transaction.save()
                    messages.success(request, f'you bought {card}')
                    return redirect('profile')
            
                else:
                    transaction.trade_choice = 0
                    transaction.save()
                    messages.error(request, 'you don\'t have enough coins. trade rejected')
                    return redirect('home')

            else:
                transaction.trade_choice = 0
                transaction.save()
                messages.error(request, 'You already have that card, you can\'t have duplicates trade rejected')
                return redirect('home')

        else:
            transaction.trade_choice = 0
            transaction.save()
            messages.error(request, 'You can\'t have more than 15 cards, trade rejected')
            return redirect('card_sales')
        
    else:
        transaction.trade_choice = 0
        transaction.save()
        return redirect('home')

@login_required
def buy_card_from_store(request, pk):
    card = get_object_or_404(Card, id=pk)
    user = request.user.profile
    user_deck = user.deck
    if not card in user_deck.all():
        if user.coins >= card.price:
            if len(user_deck.all()) <= 15:
                print(user.coins - card.price)
                user_deck.add(card)
                user.coins -= card.price
                user.save()
                messages.success(request, 'added card to deck')
            else:
                messages.error(request, 'You can\'t have more than 15 cards.')

        else:
            messages.error(request, 'You don\'t have enough coins')
    else:
        messages.error(request, 'You already have that card')
    return redirect('store')
