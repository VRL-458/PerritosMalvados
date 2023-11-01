from django.shortcuts import render, redirect
from django.http import HttpResponse
import json


from .models import Categorias, Productos,Carrito, CarritoProducto, Usuario


# Create your views here.

def productos(request):
    productos = Productos.objects.all()
    return render(request, 'producto.html', {"productos":  productos})


def anadirCarrito(request, idProducto):
    
    if request.method == 'POST':
        #if request.user.is_authenticated:
        if True:
            user_email = "luiszapatam1@upb.edu"
            
            user = Usuario.objects.get(telefono = 2)
            print("--------USUARIO AQUI---------")
            lista = list(user)
            print(lista)
            if user:
                cart, created = Carrito.objects.get_or_create(usuario_email = user, estado="ACTIVO")

                # Add the product to the cart
                cart_product, created = CarritoProducto.objects.get_or_create(carritoId=cart, productoId=idProducto)
            else:
                return redirect('http://127.0.0.1:8000/usuario/login/')
                
        else:
        # If the user is not authenticated, you can handle it as needed (e.g., show a message or prompt for login)
            return redirect('http://127.0.0.1:8000/usuario/login/')
    else:
        render(request, 'producto.html')


