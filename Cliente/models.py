from django.db import models

class Direccion (models.Model):
    id_direccion=models.AutoField(primary_key=True)
    numero_casa=models.IntegerField()
    calle=models.CharField(max_length=50)
    punto_referencia=models.CharField(max_length=50)

    class Meta:
                db_table='Direccion'
                verbose_name = 'Direccion'
                verbose_name_plural = 'Direcciones'
                ordering=['id_direccion']

    def __str__(self):
                texto = "{0} {1}"
                return texto.format(self.id_direccion,self.numero_casa)



class Cliente (models.Model):
        correo_cliente=models.CharField(primary_key=True ,max_length=50)
        id_direccion=models.ForeignKey(Direccion,on_delete=models.RESTRICT)
        nombre_cliente=models.CharField(max_length=50)
        telefono_cliente=models.CharField(max_length=15)
        password_cliente=models.CharField(max_length=9)
        puntos=models.IntegerField()
        imagen_cliente=models.ImageField(upload_to='imagen_cliente',null=True)

        class Meta:
                db_table='Cliente'
                verbose_name = 'Cliente'
                verbose_name_plural = 'Clientes'
                ordering=['correo_cliente']

        def __str__(self):
                texto = "{0} {1} {2}"
                return texto.format(self.correo_cliente,self.id_direccion,self.nombre_cliente)  

class Reclamo (models.Model):
        id_reclamo=models.AutoField(primary_key=True)
        correo_cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
        descripcion_reclamo=models.CharField(max_length=100)
        fecha_reclamo=models.DateField()

        class Meta:
                db_table='Reclamo'
                verbose_name = 'Reclamo'
                verbose_name_plural = 'Reclamos'
                ordering=['id_reclamo']

        def __str__(self):
                texto = "{0} {1}"
                return texto.format(self.correo_cliente,self.id_reclamo)  

class Pago (models.Model):
        id_pago=models.AutoField(primary_key=True)
        correo_cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
        total_pago=models.DecimalField(max_digits=8, decimal_places=2)
        tipo_pago=models.CharField(max_length=15)

        class Meta:
                db_table='Pago'
                verbose_name = 'Pago'
                verbose_name_plural = 'Pagos'
                ordering=['id_pago']

        def __str__(self):
                texto = "{0} {1}"
                return texto.format(self.correo_cliente,self.id_pago)

class Descuento (models.Model):
        id_descuento=models.AutoField(primary_key=True)
        correo=models.ForeignKey('Negocio.Usuario',on_delete=models.RESTRICT)
        correo_cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
        tipo_descuento=models.CharField(max_length=15)
        monto_desceunto=models.DecimalField(max_digits=8,decimal_places=2)
        estado_descuento=models.BooleanField(default=False)
        fecha_vencimiento=models.DateField()

        class Meta:
                db_table='Descuento'
                verbose_name = 'Descuento'
                verbose_name_plural = 'Descuentos'
                ordering=['id_descuento']

        def __str__(self):
                texto = "{0} {1}"
                return texto.format(self.correo,self.correo_cliente,self.id_descuento)


class Pedido:
        id_pedido=models.AutoField(primary_key=True)
        correo=models.ForeignKey('Negocio.Usuario',on_delete=models.RESTRICT)
        correo_cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
        id_pago=models.ForeignKey(Pago,on_delete=models.RESTRICT)
        monto_pedido=models.DecimalField(max_digits=8,decimal_places=2)
        estado_pedido=models.CharField(max_length=15)
        costo_pedido=models.DecimalField(max_digits=8,decimal_places=2)

        class Meta:
                db_table='Pedido'
                verbose_name = 'Pedido'
                verbose_name_plural = 'Pedidos'
                ordering=['id_pedido']

        def __str__(self):
                texto = "{0} {1} {2} {3}"
                return texto.format(self.id_pedido,self.correo,self.correo_cliente,self.id_pago)
