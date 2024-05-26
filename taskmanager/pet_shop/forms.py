from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):
    username = forms.CharField(max_length=150)
    surname = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password = forms.CharField()
    gender = forms.CharField(max_length=150)
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'password', 'gender', 'date_of_birth']


class ContactForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name']
