from django.shortcuts import render, redirect
from django.db.models import Sum

# Create your views here.
from .models import  Productos, Carrito, CarritoProductos, Usuario, Cotizacion, Servicios


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
           
            productos_carrito = cart.productos.all()
            
            #COTIZACIONES
            cotizacion_carrito = Cotizacion.objects.select_related('servicios').values('servicios__nombre', 'servicios__descripcion', 'servicios__imagen','precio', 'carrito', 'servicios__id').filter(carrito = cart)
   
        
            total = 0
            precio_productos = productos_carrito.aggregate(total=Sum('precio'))['total']
            precio_servicios = cotizacion_carrito.aggregate(total=Sum('precio'))['total']
            
            if(precio_productos):
                total += precio_productos
            if(precio_servicios):
                total += precio_servicios
            

            
            return render(request, 'carritos.html', {"productos_carrito": productos_carrito,"cotizacion_carrito":cotizacion_carrito ,"total":  total})
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
    
def eliminar_servicio(request, idServicio):
    if request.method == 'POST':
        global cart
        m_servicio = Servicios.objects.get(id = idServicio)
        cotizacion = Cotizacion.objects.get(servicios_id=m_servicio.id, carrito_id=cart.id)
        cotizacion.carrito = None
        cotizacion.save()
        return redirect('http://127.0.0.1:8000/carrito/carr/')
    else:
        return render(request, 'carritos.html')

    