from django.shortcuts import render, redirect
from django.db.models import Sum


# Create your views here.
from .models import Categorias, Productos, Carrito, CarritoProductos, Usuario, Cotizacion


cart = None

def carrito(request):
    if request.user.is_authenticated:
        user = request.user          
        user = Usuario.objects.get(email = user)
        cart_exists = Carrito.objects.filter(usuario_email = user, estado = 'ACTIVO').exists()
        if(cart_exists):
            
            global cart
            cart = Carrito.objects.get(usuario_email=user, estado='ACTIVO')
            
             #PRODUCTOS
            productos = Productos.objects.all()
            productos_carrito = cart.productos.all()
            
            #COTIZACIONES
            cotizaciones = Cotizacion.objects.filter(carrito = cart)
            
           
            
            total = productos_carrito.aggregate(total=Sum('precio'))['total']
            
            return render(request, 'carritos.html', {"productos_carrito": productos_carrito, "cotizaciones": cotizaciones,"total":  total})
        else:
            return render(request, 'carritos.html')
    else:
        return redirect('http://127.0.0.1:8000/usuario/login/')

def eliminar_producto(request, idProducto):
    if request.method == 'POST':
        global cart
        m_producto = Productos.objects.get(id = idProducto)
        CarritoProductos.objects.filter(carrito = cart, productos = m_producto).delete()
        return redirect('http://127.0.0.1:8000/carrito/carr/')
    else:
        return render(request, 'carritos.html')

def eliminar_carrito(request):
    if request.method == 'POST':
        global cart
        cart.estado = 'CANCELADO'
        cart.save()
        return redirect('http://127.0.0.1:8000/')
    else:
        return render(request, 'carritos.html')
    