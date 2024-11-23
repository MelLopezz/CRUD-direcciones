from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo = models.CharField(primary_key=True,max_length=50)
    nombre_usuario = models.CharField(max_length=50)
    rol_usuario = models.CharField(max_length=15)
    password_usuario = models.CharField(max_length=9)
    imagen = models.ImageField(upload_to='usuarios',null=True)

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.correo,self.nombre_usuario)
    
class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    correo = models.ForeignKey(Usuario,on_delete=models.RESTRICT)
    fecha_menu = models.DateField(auto_now=False)

    class Meta:
        db_table = 'Menu'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.id_menu,self.correo)
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    correo = models.ForeignKey(Usuario,on_delete=models.RESTRICT)
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.DecimalField(max_digits=8,decimal_places=2)
    disponibilidad_producto = models.BooleanField(default=False)
    descripcion_producto = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos',null=True)

    class Meta:
        db_table = 'Productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.id_producto,self.nombre_producto)


class Detalle_Menu(models.Model):
    id_detalle_menu = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey(Menu,on_delete=models.RESTRICT)
    id_producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Detalle_Menu'
        verbose_name = 'Detalle_Menu'
        verbose_name_plural = 'Detalles_Menus'

    def __str__(self):
        texto = "{0} {1} {2}"
        return texto.format(self.id_detalle_menu,self.id_detalle_menu,self.id_producto)
    

