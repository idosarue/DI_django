from .models import Customer, Rental
from django import forms
from phonenumber_field.formfields import PhoneNumberField

def validate_customer_id(customer_id):
    if not Customer.objects.filter(id=customer_id).exists():
        raise forms.ValidationError(f'The customer does not exist.')

def validate_vehicle_id(vehicle_id):
    if not Rental.objects.filter(id=vehicle_id).exists():
        raise forms.ValidationError(f'The vehicle does not exist.')
    else:
        vehicle = Rental.objects.get(id=vehicle_id)
        if not vehicle.is_returned():
            raise forms.ValidationError('The vehicle is currently rented.')


class RentForm(forms.Form):
    vehicle_id = forms.IntegerField(min_value=1,
          label="vehicle id", 
        #   help_text='Must contain al least 8 characters', 
          error_messages={'required': 'Please enter a value'},
           widget= forms.TextInput(attrs={'placeholder':'Kia'}),
        validators=[validate_vehicle_id])
    customer_id = forms.IntegerField(min_value=1, 
        error_messages={'required': 'Please enter a value'},
        widget= forms.TextInput(attrs={'placeholder':'Kia'}),
        validators=[validate_customer_id])

class AddCustomerForm(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    address = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)
