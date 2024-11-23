# Generated by Django 5.0.1 on 2024-11-23 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_menu', models.DateField()),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'db_table': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('disponibilidad_producto', models.BooleanField(default=False)),
                ('descripcion_producto', models.CharField(max_length=50)),
                ('imagen_producto', models.ImageField(null=True, upload_to='productos')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('rol_usuario', models.CharField(max_length=15)),
                ('password_usuario', models.CharField(max_length=9)),
                ('imagen', models.ImageField(null=True, upload_to='usuarios')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Detalle_Menu',
            fields=[
                ('id_detalle_menu', models.AutoField(primary_key=True, serialize=False)),
                ('id_menu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Negocio.menu')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Negocio.producto')),
            ],
            options={
                'verbose_name': 'Detalle_Menu',
                'verbose_name_plural': 'Detalles_Menus',
                'db_table': 'Detalle_Menu',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='correo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Negocio.usuario'),
        ),
        migrations.AddField(
            model_name='menu',
            name='correo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Negocio.usuario'),
        ),
    ]
