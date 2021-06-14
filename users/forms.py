from django import forms
from django.forms import BooleanField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    choice = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'choice', 'password1', 'password2']

