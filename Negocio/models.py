from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo = models.CharField(primary_key=True,max_length=50)
    nombre_usuario = models.CharField(max_length=50)
    rol_usuario = models.CharField(max_length=5)
    password_usuario = models.CharField(max_length=9)

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.correo,self.nombre_usuario)