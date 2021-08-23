from .models import Customer, Rental, Vehicle, VehicleSize, VehicleType
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.forms import ModelForm
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

def validate_customer_email(email):
    if Customer.objects.filter(email=email).exists():
        raise forms.ValidationError('The email already exists.')


def validate_customer_phone(phone_number):
    if Customer.objects.filter(phone_number=phone_number).exists():
        raise forms.ValidationError('The phone number already exists.')


class RentForm(forms.Form):
    vehicle_id = forms.IntegerField(min_value=1,
          label="vehicle id", 
        #   help_text='Must contain al least 8 characters', 
          error_messages={'required': 'Please enter a value'},
           widget= forms.TextInput(attrs={'placeholder':'Vehicle Id'}),
        validators=[validate_vehicle_id])
    customer_id = forms.IntegerField(min_value=1, 
        error_messages={'required': 'Please enter a value'},
        widget= forms.TextInput(attrs={'placeholder':'Customer Id'}),
        validators=[validate_customer_id])

class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10,
    widget= forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30,
    widget= forms.TextInput(attrs={'placeholder':'Last Name'}))
    
   
    email = forms.EmailField(
        error_messages={'required': 'Please enter a value'},
       widget= forms.TextInput(attrs={'placeholder':'Email'}),
       validators=[validate_customer_email]
    )
    phone_number = PhoneNumberField(
        error_messages={'required': 'Please enter a value'},
       widget= forms.TextInput(attrs={'placeholder':'Phone Number'}),
       validators=[validate_customer_phone]
    )
    address = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)


class AddVehicleForm(forms.Form):
    vehicle = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())

    def prices(self):
        if self.size == 'very big':
            self.real = 1000
