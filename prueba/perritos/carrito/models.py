# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class Carrito(models.Model):
    id = models.IntegerField(primary_key=True)
    fechacreacion = models.DateField()
    estado = models.CharField(max_length=50)
    usuario_email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_email')
    productos = models.ManyToManyField('Productos', through='CarritoProductos')
    servicios = models.ManyToManyField("Servicios", through='Cotizacion')
    class Meta:
        managed = False
        db_table = 'carrito'


class CarritoProductos(models.Model):
    carrito = models.OneToOneField(Carrito, models.DO_NOTHING, primary_key=True)  # The composite primary key (carrito_id, productos_id) found, that is not supported. The first column is selected.
    productos = models.ForeignKey('Productos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carrito_productos'
        unique_together = (('carrito', 'productos'),)


class Categorias(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categorias'


class Compra(models.Model):
    id = models.IntegerField(primary_key=True)
    metodopago = models.CharField(max_length=50)
    fecha = models.DateField()
    departamento = models.CharField(max_length=50)
    ciuddad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    contacto = models.IntegerField()
    observaciones = models.CharField(max_length=100)
    numerotarjeta = models.IntegerField()
    nombrepropietariotarjeta = models.CharField(max_length=100)
    fechaexpiraciontarjeta = models.DateField()
    numeroscvv = models.IntegerField()
    factura = models.ForeignKey('Factura', models.DO_NOTHING)
    carrito = models.ForeignKey(Carrito, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'


class Cotizacion(models.Model):
    id = models.IntegerField(primary_key=True)
    fechaCreacion = models.DateField()
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    fechaFinalizacion = models.DateField(blank=True, null=True)
    servicios = models.ForeignKey('Servicios', models.DO_NOTHING)
    carrito = models.ForeignKey(Carrito, models.DO_NOTHING)
    precio = models.IntegerField()
    usuario_email = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='%(class)s_usuarios', db_column='usuario_email')
    encargadoVentas_email = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='%(class)s_encargados', db_column='encargadoVentas_email')

    class Meta:
        managed = False
        db_table = 'cotizacion'



class Encargadoventas(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    date_joined = models.DateTimeField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'encargadoventas'







class Factura(models.Model):
    id = models.IntegerField(primary_key=True)
    nit = models.IntegerField()
    razonsocial = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'factura'


class Productos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
    categorias = models.ForeignKey(Categorias, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productos'





class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
   
    class Meta:
        managed = False
        db_table = 'servicios'


class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    date_joined = models.DateTimeField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuario'
