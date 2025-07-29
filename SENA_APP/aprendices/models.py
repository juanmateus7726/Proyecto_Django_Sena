from django.db import models

# Create your models here.
class aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=20, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=100, null=True)
    programa = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento_identidad}"
