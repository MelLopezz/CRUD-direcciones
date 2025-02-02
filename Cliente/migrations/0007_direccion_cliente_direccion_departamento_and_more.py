# Generated by Django 5.1.3 on 2024-12-02 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0006_remove_cliente_id_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='Cliente.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='departamento',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='municipio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='nombre_direccion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
