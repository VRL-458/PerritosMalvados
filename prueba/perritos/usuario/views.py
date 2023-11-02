from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, get_user_model
# Create your views here.
from .forms import CreateUser, LoginForm, RegistrarFactura, RegistrarCompra


from .models import Usuario, Carrito, Factura, Compra, Cotizacion
from django.utils import timezone
from datetime import date
def registro(request):
    return render(request, 'registro.html')
def perfil(request):
    return render(request, 'perfil.html')


def ventas(request):
    return render(request, 'venta.html')


def login_view(request):
    Usuarios = Usuario.objects.all()
    return render(request, 'login.html', {"Usuarios": Usuarios})


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
            user = authenticate(request, email=email, password=password)
            try:
                user = Usuario.objects.get(email=email)
                if user.check_password(password):
                    login(request, user) #esto hcace el login :)
                    return redirect('http://127.0.0.1:8000/')
                else:
                    mensaje = "Contraseña incorrecta."
            except Usuario.DoesNotExist:
                mensaje = "El Usuario no existe."

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'mensaje': mensaje, 'user': request.user})




def some_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hola, {request.user.email}!")
    else:
        return HttpResponse("Por favor, inicia sesión.")





def factura(request, factura_id):
    # Obtén la factura desde la base de datos
    factura = get_object_or_404(Factura, id=factura_id)

    # Obtén todas las compras relacionadas con esta factura
    compra = get_object_or_404(Compra, factura=factura_id)

    detalles_productos = []
    detalles_cotizaciones = []

    # Recorre todas las compras y obtén los detalles de productos y cotizaciones
    carrito = compra.carrito

    # Obtén las cotizaciones relacionadas con el carrito
    cotizaciones_del_carrito = carrito.cotizacion_set.all()

    # Obtén los productos relacionados con el carrito a través de CarritoProductos
    productos_del_carrito = carrito.productos.all()

    # Agrega los detalles de productos y cotizaciones a las listas correspondientes
    detalles_productos.extend(productos_del_carrito)
    detalles_cotizaciones.extend(cotizaciones_del_carrito)

    Usuario = carrito.usuario_email

    total = 0
    for producto in detalles_productos:
        total += producto.precio
    for cotizacion in detalles_cotizaciones:
        total += cotizacion.precio

    return render(request, 'factura.html', {
        'factura': factura,
        'compra' : compra,
        'detalles_productos': detalles_productos,
        'detalles_cotizaciones': detalles_cotizaciones,
        'Usuario': Usuario,
        'total': total,
    })


def procesar_compra(request):
    if request.method == 'POST':
        factura_form = RegistrarFactura(request.POST)
        compra_form = RegistrarCompra(request.POST)


        if factura_form.is_valid() and compra_form.is_valid():
            print("Formulario válido")

            #recibir email registrado
            email = request.user.email
            carrito = Carrito.objects.get(usuario_email=email, estado='Activo')
            carrito.estado = "Comprado"
            carrito.save()

            stockSuficiente = True

            productos_del_carrito = carrito.productos.all()
            for producto in productos_del_carrito:
                producto.stock -= 1
                if producto.stock < 0:
                    stockSuficiente = False
                producto.save()
            if stockSuficiente:

                # Guardar la factura en la base de datos
                factura = factura_form.save()
                # Guardar la compra en la base de datos con la factura asociada
                compra = compra_form.save(commit=False)  # commit=False evita que se guarde la compra automáticamente
                compra.factura = factura  # Establecer la relación con la factura
                compra.carrito = carrito
                compra.metodopago = 'Tarjeta'
                compra.fecha = date.today()
                compra.save()  # Guardar la compra
                # Realizar cualquier acción adicional que necesites y luego redirigir
                return redirect('factura', factura_id=factura.id)
        else:
            print("Formulario NO válido")
    return render(request, 'venta.html')
