# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categorias'


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
    carrito = models.ForeignKey(Carrito, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Encargadoventas(models.Model):
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
        db_table = 'encargadoventas'


class Factura(models.Model):
    nit = models.IntegerField()
    razonsocial = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'factura'


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


class ProductosCategorias(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'productos_categorias'


class ProductosProductos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
    categorias = models.ForeignKey(ProductosCategorias, models.DO_NOTHING, db_column='Categorias_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos_productos'


class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'servicios'


class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    date_joined = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuario'
