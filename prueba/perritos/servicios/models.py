from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission, Group
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class EncargadoManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El campo email es requerido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Encargado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True, unique=True, max_length=255)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(Group, blank=True, related_name="encargado_user_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="encargado_user_set")

    objects = EncargadoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        managed = False  # Asegúrate de gestionar este modelo
        db_table = 'encargadoventas'

    def check_password(self, raw_password):
        return self.password == raw_password

    @property
    def is_authenticated(self):
        return True

class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'servicios'


class Cotizacion(models.Model):
    fechaCreacion = models.DateField(auto_now_add=True, auto_now=False)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50,default='En espera')
    fechaFinalizacion = models.DateField(auto_now_add=False, auto_now=True)
    servicios_id = models.IntegerField()
    carrito_id = models.IntegerField()
    precio = models.IntegerField()
    usuario_email = models.CharField(max_length=50)
    encargadoVentas_email = models.CharField(max_length=50)
