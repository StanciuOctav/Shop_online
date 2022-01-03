from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserSignUpForm(forms.Form, UserCreationForm):
    email = forms.EmailField(max_length=100)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
