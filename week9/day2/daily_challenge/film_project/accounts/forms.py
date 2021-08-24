from django import forms
from .models import NewUser

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = NewUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        password_2 = cleaned_data["password_2"]
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data
