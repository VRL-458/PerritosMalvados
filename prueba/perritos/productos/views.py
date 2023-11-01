from django.shortcuts import render, redirect
from django.http import HttpResponse
import json


from .models import Categorias, Productos, Carrito, CarritoProductos, Usuario


# Create your views here.

def productos(request):
    productos = Productos.objects.all()
    return render(request, 'producto.html', {"productos":  productos})


def anadirCarrito(request, idProducto):
    
    if request.method == 'POST':
        #if request.user.is_authenticated:
        if True:
            try:
                #user = request.user
                
                todo = Usuario.objects.all()
                
                u_email = "luiszapatam1@upb.edu"
                user = Usuario.objects.get(email = u_email)
                cart, created = Carrito.objects.get(usuario_email = u_email)
                
                
            except Usuario.DoesNotExist:
                print("------Usuario no encontrado o no se---------")
                return redirect('http://127.0.0.1:8000/usuario/login/')
            except Carrito.DoesNotExist:
                cart = Carrito.objects.create(usuario_email=user, estado="ACTIVO")
                
            cart_product, created = CarritoProductos.objects.get_or_create(carritoId=cart, productoId=idProducto)
        else:
        # If the user is not authenticated, you can handle it as needed (e.g., show a message or prompt for login)
            return redirect('http://127.0.0.1:8000/usuario/login/')
    else:
        render(request, 'producto.html')


