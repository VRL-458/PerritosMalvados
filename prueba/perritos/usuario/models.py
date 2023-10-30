from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
