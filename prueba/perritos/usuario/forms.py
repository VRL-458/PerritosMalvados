from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Factura, Compra

class CreateUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellido', 'password', 'telefono')

class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput, label="password")



class RegistrarFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('nit', 'razonsocial')

class RegistrarCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('departamento', 'ciuddad', 'direccion', 'contacto', 'observaciones', 'numerotarjeta', 'nombrepropietariotarjeta', 'fechaexpiraciontarjeta', 'numeroscvv')