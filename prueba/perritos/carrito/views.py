from django.shortcuts import render
from .models import Carrito, CarritoProducto

# Create your views here.

def carrito(request):
    
    #Obtener carrito actual del usuario
    productos_carrito = productos_carrito.objects.all(carritoId = 1)
    return render(request, 'carritos.html', {"productos_carrito", productos_carrito})



