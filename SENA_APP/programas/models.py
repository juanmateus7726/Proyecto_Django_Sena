from django.db import models

class Programa(models.Model):
    NIVEL_FORMACION_CHOICES =[
        ('AUX', 'Auxiliar'),
        ('OPE', 'Operario'),
        ('TEC', 'Tecnico'),
        ('TGL', 'Tecnologo'),
        ('ESP', 'Especializacion Tecnologica'),
        ('COM', 'Complementario'),
    ]
    
    MODALIDAD_CHOICES = [
        ('PRE', 'Presencial'),
        ('VIR', 'Virtual'),
        ('MIX', 'Mixta'),
    ]
    
    ESTADO_CHOICES = [
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
        ('SUS', 'Suspendido'),
        ('CAN', 'Cancelado'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Codigo del Programa")
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Programa")
    nivel_formacion = models.CharField(max_length=3, choices=NIVEL_FORMACION_CHOICES, verbose_name="Nivel de Formacion")
    modalidad = models.CharField(max_length=3, choices=MODALIDAD_CHOICES, default='PRE', verbose_name="Modalidad")
    duracion_meses = models.PositiveIntegerField(verbose_name="Duracion en meses")
    duracion_horas = models.PositiveIntegerField(verbose_name="Duracion en Horas")
    descripcion = models.TextField(verbose_name="Descripcion del Programa")
    competencias = models.TextField(verbose_name="Competencias a Desarrollar")
    perfil_egreso = models.TextField(verbose_name="Pefil de Egreso")
    requisitos = models.TextField(verbose_name="Requisitos de Ingreso")
    centro_formacion = models.CharField(max_length=200, verbose_name="Centro de Formacion")
    regional = models.CharField(max_length=100, verbose_name="Regional")
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='ACT', verbose_name="Estado")
    fecha_creacion = models.DateField(verbose_name="Fecha de Creacion del Programa")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Programa de Formacion"
        verbose_name_plural = "Programas de Formacion"
        ordering = ['nombre']
        
        def __srt__(self):
            return f"{self.codigo} - {self.nombre}"
        
        def get_duracion_completa(self):
            return f"{self.duracion_meses} meses ({self.duracion_horas} horas)"
        
        def is_activo(self):
            return self.estado == 'ACT'