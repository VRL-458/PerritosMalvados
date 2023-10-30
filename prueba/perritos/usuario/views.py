from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, get_user_model
# Create your views here.
from .forms import CreateUser, LoginForm

from .models import Usuario
def registro(request):
    return render(request, 'registro.html')
def perfil(request):
    return render(request, 'perfil.html')


def ventas(request):
    return render(request, 'venta.html')


def login(request):
    usuarios = Usuario.objects.all()
    return render(request, 'login.html', {"usuarios": usuarios})


def registros(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = CreateUser()
    return render(request, 'registro.html', {'form': form})



def authenticate_email(email, password):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=email)
        if user.check_password(password):
            return user
    except UserModel.DoesNotExist:
        return None



def user_login(request):
    mensaje = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Usuario.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/')
                else:
                    mensaje = "Contraseña incorrecta."
            except Usuario.DoesNotExist:
                mensaje = "El usuario no existe."

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'mensaje': mensaje})