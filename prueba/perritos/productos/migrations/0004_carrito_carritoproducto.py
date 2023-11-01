# Generated by Django 4.2.6 on 2023-10-31 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_delete_productoscategorias_delete_productosproductos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('usuario_email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'carrito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carritoId', models.IntegerField()),
                ('productoId', models.IntegerField()),
            ],
            options={
                'db_table': 'carrito_productos',
                'managed': False,
            },
        ),
    ]