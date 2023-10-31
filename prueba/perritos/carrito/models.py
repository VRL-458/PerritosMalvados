from django.db import models

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
