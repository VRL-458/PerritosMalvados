# Generated by Django 4.2.6 on 2023-11-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_cotizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='estado',
            field=models.CharField(default='En espera', max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fechaFinalizacion',
            field=models.DateField(auto_now=True),
        ),
    ]