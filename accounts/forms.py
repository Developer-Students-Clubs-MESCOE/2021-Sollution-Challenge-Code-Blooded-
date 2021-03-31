from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class' : 'form-control'}) )
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class Meta:
            model = User
            fields = ('username', 'password1', 'password2', 'first_name', 'last_name',  'email')




