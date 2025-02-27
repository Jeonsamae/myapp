from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    occupation = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'occupation', 'company', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
