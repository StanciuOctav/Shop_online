from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserSignUpForm(forms.Form, UserCreationForm):
    email = forms.EmailField(max_length=100)
