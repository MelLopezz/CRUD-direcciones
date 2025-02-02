# Generated by Django 5.0.1 on 2024-11-23 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Negocio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('correo_cliente', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(max_length=15)),
                ('password_cliente', models.CharField(max_length=9)),
                ('puntos', models.IntegerField()),
                ('imagen_cliente', models.ImageField(null=True, upload_to='imagen_cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('numero_casa', models.IntegerField()),
                ('calle', models.CharField(max_length=50)),
                ('punto_referencia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id_descuento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_descuento', models.CharField(max_length=15)),
                ('monto_desceunto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado_descuento', models.BooleanField(default=False)),
                ('fecha_vencimiento', models.DateField()),
                ('correo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Negocio.usuario')),
                ('correo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Cliente.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Cliente.direccion'),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo_pago', models.CharField(max_length=15)),
                ('correo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id_reclamo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_reclamo', models.CharField(max_length=100)),
                ('fecha_reclamo', models.DateField()),
                ('correo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Cliente.cliente')),
            ],
        ),
    ]
