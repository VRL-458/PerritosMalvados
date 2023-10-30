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





