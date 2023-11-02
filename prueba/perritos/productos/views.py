from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import json


from .models import Categorias, Productos, Carrito, CarritoProductos, Usuario


# Create your views here.

def productos(request):
    productos = Productos.objects.all()
    return render(request, 'producto.html', {"productos":  productos})


def anadirCarrito(request, idProducto):
    
    if request.method == 'POST':
        if request.user.is_authenticated:

            try:
                user = request.user
                user = Usuario.objects.get(email = user)
                cart_exists = Carrito.objects.filter(usuario_email = user, estado = 'ACTIVO').exists()
                
            except Usuario.DoesNotExist:
                return redirect('http://127.0.0.1:8000/usuario/login/')
            
            if(not cart_exists):
                current_date = timezone.now().date()
                Carrito.objects.create(usuario_email=user, estado='ACTIVO', fechacreacion = current_date)
            cart = Carrito.objects.get(usuario_email=user, estado='ACTIVO')
            
            
            producto = Productos.objects.get(id = idProducto)
            
            producto_carrito = CarritoProductos.objects.filter(carrito=cart, productos = producto).exists()
            if(not producto_carrito):
                CarritoProductos.objects.create(carrito=cart, productos = producto)
            return redirect('http://127.0.0.1:8000/productos/pro/')
        else:
        # If the user is not authenticated, you can handle it as needed (e.g., show a message or prompt for login)
            return redirect('http://127.0.0.1:8000/usuario/login/')
    else:
        render(request, 'producto.html')

