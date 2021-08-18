
from django import forms
from phonenumber_field.formfields import PhoneNumberField



class AddPersonForm(forms.Form):
    name = forms.CharField(max_length=2)
    email = forms.EmailField(max_length=30)
    phone_number = PhoneNumberField()
    address = forms.CharField(max_length=20)

def check(phone_number):
    if not phone_number:
        print('asd')
        raise forms.ValidationError('One of fields is required')

class SearchPersonForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    phone_number = PhoneNumberField(required=False,
    validators=[check], # Call the validate_name function here
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write your name here'
    }))
    
