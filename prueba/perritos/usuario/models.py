from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission, Group
# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone



class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El campo email es requerido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True, unique=True, max_length=255)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    roles = models.CharField(max_length=50, default='usuario')

    groups = models.ManyToManyField(Group, blank=True, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="custom_user_set")

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        managed = False
        db_table = 'usuario'

    def check_password(self, raw_password):
        return self.password == raw_password

    @property
    def is_authenticated(self):
        return True


class Carrito(models.Model):
    fechacreacion = models.DateField()
    estado = models.CharField(max_length=50)
    usuario_email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_email')
    productos = models.ManyToManyField('Productos', through='CarritoProductos')

    class Meta:
        managed = False
        db_table = 'carrito'

class Factura(models.Model):
    nit = models.IntegerField()
    razonsocial = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'factura'


class Compra(models.Model):
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
    carrito = models.ForeignKey('Carrito', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'

class CarritoProductos(models.Model):
    carrito = models.OneToOneField(Carrito, models.DO_NOTHING, primary_key=True)  # The composite primary key (carrito_id, productos_id) found, that is not supported. The first column is selected.
    productos = models.ForeignKey('Productos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carrito_productos'
        unique_together = (('carrito', 'productos'),)

class Encargadoventas(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'encargadoventas'

class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'servicios'

class Cotizacion(models.Model):
    fechacreacion = models.DateField()
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    fechafinalizacion = models.DateField(blank=True, null=True)
    servicios = models.ForeignKey('Servicios', models.DO_NOTHING)
    carrito = models.ForeignKey(Carrito, models.DO_NOTHING)
    precio = models.IntegerField()
    usuario_email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_email')
    encargadoventas_email = models.ForeignKey('Encargadoventas', models.DO_NOTHING, db_column='encargadoventas_email')

    class Meta:
        managed = False
        db_table = 'cotizacion'

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categorias'

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
    categorias = models.ForeignKey(Categorias, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productos'
