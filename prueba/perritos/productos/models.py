from django.db import models

# Create your models here.

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


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categorias'

class Productos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=400)
    imagen = models.CharField(max_length=30000)
    categorias = models.ForeignKey(Categorias, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productos'
        
class Carrito(models.Model):
    fechacreacion = models.DateField()
    estado = models.CharField(max_length=50)
    usuario_email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_email')

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





