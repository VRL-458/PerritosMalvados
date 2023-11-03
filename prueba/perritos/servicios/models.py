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
