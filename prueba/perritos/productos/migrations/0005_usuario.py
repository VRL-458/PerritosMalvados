# Generated by Django 4.2.6 on 2023-11-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_carrito_carritoproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
