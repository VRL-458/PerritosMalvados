from django.db import models

# Create your models here.


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
        
class Carrito(models.Model):
    id = models.IntegerField(primary_key=True)
    fechaCreacion = models.DateField()
    estado = models.CharField(max_length=50)
    usuario_email = models.CharField(max_length=50)
    

    class Meta:
        managed = False
        db_table = 'carrito'
        
class CarritoProducto(models.Model):
    carritoId = models.IntegerField()
    productoId = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carrito_productos'





