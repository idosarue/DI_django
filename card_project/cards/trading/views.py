from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TransactionForm
from .models import Card, Transaction
from accounts.models import Profile

def home(request):
    return render(request, 'trading/home.html')
class TransactionListView(ListView):
    model = Transaction
    template_name = 'trading/home.html'
    
class CreateTradeView(CreateView):
    form_class = TransactionForm
    template_name = 'trading/create_trade.html'
    success_url = reverse_lazy('home')

    # def post(self, request, *args: str, **kwargs) :
    #     card = self.request.POST
    #     print(card['cards'])
    #     return super().post(request, *args, **kwargs)

    def form_valid(self, form): 
        transaction = form.save(commit=False)
        data = self.request.POST
        transaction.card = Card.objects.get(name=data['cards'])
        transaction.trade_sender = self.request.user.profile
        transaction.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = self.request.user.profile.deck.all()
        return context
