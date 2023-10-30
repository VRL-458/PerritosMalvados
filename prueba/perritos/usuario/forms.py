from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CreateUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'password', 'email', 'telefono')

class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput, label="password")
