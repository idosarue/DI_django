from django.http import request, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.db.models import F 
from .models import *
from .forms import *
from datetime import datetime
# Create your views here.

    # rental_date = models.DateField()
    # return_date = models.DateField(null=True)
    # customer = models.ForeignKey(Customer, on_delete=CASCADE)
    # vehicle =
def rent(request):
    f = Rental.objects.all().order_by(F('return_date').asc(nulls_last=False))
    return render(request, 'rental.html', {'rentals' : f})

def rental_details(request, pk):
    f = get_object_or_404(Rental, pk=pk)
    print(f)
    return render(request, 'rental_details.html', {'details' : f})

def display_rental_details(request, pk):
    f = get_object_or_404(Rental, pk=pk)
    return redirect('rental_details', pk) 

def add_rental(request):
    if request.method == 'GET':
        form = RentForm()
    elif request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            x= form.cleaned_data['vehicle_id']
            vehicle = Rental.objects.get(id=x)
            vehicle.return_date = None
            vehicle.save()
    return render(request, 'add.html', {'form' : form})

def show_customer(request, pk):
    f = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer.html', {'customer' : f})

def show_customers(request):
    f = Customer.objects.all().order_by('first_name')
    return render(request, 'customers.html', {'customers' : f})