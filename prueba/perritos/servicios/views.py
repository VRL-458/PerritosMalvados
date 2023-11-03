from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Servicios, Cotizacion
import sys
sys.path.append("..")
from usuario.models import Usuario
from carrito.models import Carrito
from django.utils import timezone

    
def servicios_view(request):
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
                if user.roles == 'encargado':
                    return HttpResponse("Usted es un ENCARGADO. No puede realizar cotizaciones!")
                
            except Usuario.DoesNotExist:
                return redirect('http://127.0.0.1:8000/usuario/login/')

            if request.POST.get('descripcion'):
                cotizacion = Cotizacion()
                cotizacion.descripcion = request.POST.get('descripcion')
                cotizacion.servicios_id = id_servicio
                cotizacion.usuario_email = user.email
                cotizacion.encargadoVentas_email = None
                cotizacion.save()
                return redirect('http://127.0.0.1:8000/servicios/ser')
        else:
            return redirect('http://127.0.0.1:8000/usuario/login/')

    return render(request, 'cotizacion.html', {'nombre_servicio': servicio.nombre, 'imagen_servicio': servicio.imagen})

def revisar_cotizaciones(request):
    print(request.user)

    if request.method == "POST":
        print(request.POST.get('precio'))
        print(request.POST.get('id_servicio'))

        if request.POST.get('precio') and request.POST.get('id_servicio'):
            _user = request.user
            _precio = request.POST.get('precio')
            _cotizacion = request.POST.get('id_servicio')

            _cotizacion_obj = Cotizacion.objects.get(id=_cotizacion)
            _carrito_existe = Carrito.objects.filter(usuario_email=_cotizacion_obj.usuario_email, estado='ACTIVO').exists()
            if not _carrito_existe:
                usuario = Usuario.objects.filter(email=_cotizacion_obj.usuario_email)
                print(usuario)
                current_date = timezone.now().date()
                Carrito.objects.create(usuario_email=usuario, estado='ACTIVO', fechacreacion = current_date)
                
            _carrito = Carrito.objects.get(usuario_email=_cotizacion_obj.usuario_email, estado='ACTIVO')

            _cotizacion_obj.carrito_id = _carrito.id 
            _cotizacion_obj.encargadoVentas_email = str(_user)
            _cotizacion_obj.precio = _precio
            _cotizacion_obj.estado = 'Respondido'
            _cotizacion_obj.save()

        return redirect('http://127.0.0.1:8000/servicios/revisar_cotizaciones')
        

    else:
        if request.user.is_authenticated:
            try:
                user = request.user
                user = Usuario.objects.get(email = user)
                if user.roles == 'encargado':
                    cotizaciones = Cotizacion.objects.filter(estado='En espera')
                    return render(request, 'revisar_cotizaciones.html', {'cotizaciones': cotizaciones})
                else:
                    return HttpResponse("No tiene permiso para ver esta página")

            except Usuario.DoesNotExist:
                print("No existe el usuario")
                return redirect('http://127.0.0.1:8000/usuario/login')
        else:
            print("Nadie ha iniciado sesión")
            return redirect('http://127.0.0.1:8000/usuario/login')
