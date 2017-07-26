from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    first_name = forms.CharField(label="First Name", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))
    last_name = forms.CharField(label="Last Name", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}))
    email = forms.CharField(label="Email", max_length=60,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))
    password1 = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'}))
    password2 = forms.CharField(label="Confirm Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )