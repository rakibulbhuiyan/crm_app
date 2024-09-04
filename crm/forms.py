from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Record


class SignupForm(UserCreationForm):
    Name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['Name', 'email', 'username', 'password1', 'password2']


class Addrecord(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone No', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_image = forms.ImageField(label='profile_image')

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'state', 'profile_image']
