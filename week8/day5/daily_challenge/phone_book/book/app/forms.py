
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class AddPersonForm(forms.Form):
    name = forms.CharField(max_length=2)
    email = forms.EmailField(max_length=30)
    phone_number = PhoneNumberField(
        widget = PhoneNumberInternationalFallbackWidget()
    )
    address = forms.CharField(max_length=20)

def check(phone_number):
    if not phone_number:
        print('asd')
        raise forms.ValidationError('One of fields is required')

class SearchPersonForm(forms.Form):
    name = forms.CharField(max_length=20)
    phone_number = PhoneNumberField(
    validators=[check], # Call the validate_name function here
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write your name here'
    }))
    

