from django.db import models

# Create your models here.
class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'servicios'