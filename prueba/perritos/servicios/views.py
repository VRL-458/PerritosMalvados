from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Encargado,  Servicios, Cotizacion
import sys
sys.path.append("..")
from usuario.models import Usuario
from carrito.models import Carrito
from .forms import LoginEncargado
from django.utils import timezone


def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios.html', {"servicios": servicios})

def cotizacion(request):
    return render(request, 'cotizacion.html', )


def login_view_encargado(request):
    encargado = Encargado.objects.all()
    return render(request, 'encargado_login.html', {"encargado": encargado})

def encargado_login(request):
    mensaje = ""
    if request.method == 'POST':
        form = LoginEncargado(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            try:
                encargado = Encargado.objects.get(email=email)
                if encargado.check_password(password):
                    login(request, encargado) # Inicia sesión como encargado
                    return redirect('http://127.0.0.1:8000/')
                else:
                    mensaje = "Contraseña incorrecta."
            except Encargado.DoesNotExist:
                mensaje = "El encargado no existe."

    else:
        form = LoginEncargado()

    return render(request, 'encargado_login.html', {'form': form, 'mensaje': mensaje, 'user': request.user})


def some_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hola, {request.user.email}!")
    else:
        return HttpResponse("Por favor, inicia sesión.")
    
def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios.html', {"servicios": servicios})

def cotizacion(request):
    id_servicio = request.GET.get('id_servicio', None)
    servicio = Servicios.objects.get(pk=id_servicio)

    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                user = request.user
                user = Usuario.objects.get(email = user)
                
            except Usuario.DoesNotExist:
                return redirect('http://127.0.0.1:8000/usuario/login/')

            if request.POST.get('descripcion'):
                cotizacion = Cotizacion()
                cotizacion.descripcion = request.POST.get('descripcion');
                cotizacion.servicios_id = id_servicio
                cotizacion.usuario_email = user.email
                cotizacion.save()
                print("Cotización enviada")

                

    return render(request, 'cotizacion.html', {'nombre_servicio': servicio.nombre, 'imagen_servicio': servicio.imagen})
