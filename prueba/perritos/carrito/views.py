from django.shortcuts import render
from .models import Carrito, CarritoProducto

# Create your views here.

def carrito(request):
    
    #Obtener carrito actual del usuario
    carrito = CarritoProducto.objects.all()
    return render(request, 'carritos.html', {"productos_carrito", carrito})



