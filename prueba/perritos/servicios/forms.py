from django import forms

from .models import Encargado


class LoginEncargado(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput, label="password")
