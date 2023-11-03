from django.db import models


class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=30000)

    class Meta:
        managed = False
        db_table = 'servicios'


class Cotizacion(models.Model):
    fechaCreacion = models.DateField(auto_now_add=True, auto_now=False)
    descripcion = models.CharField(max_length=1000)
    estado = models.CharField(max_length=50,default='En espera')
    fechaFinalizacion = models.DateField(auto_now_add=False, auto_now=True)
    servicios_id = models.IntegerField()
    carrito_id = models.IntegerField()
    precio = models.IntegerField()
    usuario_email = models.CharField(max_length=50)
    encargadoVentas_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cotizacion'


class Carrito(models.Model):
    fechacreacion = models.DateField()
    estado = models.CharField(max_length=50)
    usuario_email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_email')

    class Meta:
        managed = False
        db_table = 'carrito'


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
    roles = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'