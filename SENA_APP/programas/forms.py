from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=10, label="Codigo", help_text="Ingrese el codigo del programa")
    nombre = forms.CharField(max_length=100, label="Nombre", help_text="Ingrese el nombre del programa.")
    nivel_formacion = forms.ChoiceField(choices=Programa.NIVEL_FORMACION_CHOICES, label="Nivel de Formacion", help_text="Ingrese el nivel de formacion.")
    modalidad = forms.ChoiceField(choices=Programa.MODALIDAD_CHOICES, label="Modalidad", help_text="Ingresa la modalidad.")
    duracion_meses = forms.CharField(max_length=20, label="Duracion de Meses", help_text="Ingrese la duracion de meses del programa.")
    duracion_horas = forms.CharField(max_length=100, label="Duracion de Horas", help_text="Ingrese la duracion de Horas del programa.")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripcion", help_text="Ingrese la descripcion del programa")
    competencias = forms.CharField(widget=forms.Textarea, label="Competencias", help_text="Ingrese las competencias del programa.")
    perfil_egreso = forms.CharField(max_length=100, required=False, label="Perfil de egresado", help_text="Ingrese el Perfil de Egresado")
    requisitos = forms.CharField(max_length=200, required=False, label="Requisitos", help_text="Ingrese los requisitos")
    centro_formacion = forms.CharField(max_length=100, label="Centro de Formacion", help_text="Ingrese el centro de formacion")
    regional = forms.CharField(max_length=100, label="Regional", help_text="Ingrese la regional.")
    estado = forms.CharField(max_length=50, label="Estado", help_text="Ingrese el estado")
    fecha_creacion = forms.DateField(label="Fecha de Creacion", help_text="Ingresa la fecha de creacion.")
    fecha_registro = forms.DateField(required=False, label="Fecha de Registro", help_text="Ingrese la fecha de registro.")
    
    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')
        nivel = cleaned_data.get('nivel_formacion')
        print(f"Valores: {codigo} (codigo), {nombre} (nombre), {nivel} (nivel)")
        if not all([codigo, nombre, nivel]):
            raise forms.ValidationError("Todos los campos son obligatorios.")
        
        return cleaned_data
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isdigit():
            raise forms.ValidationError("El documento solo debe de contener numeros.")
        return codigo
    
    def save(self):
        try:
            nuevo_programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                modalidad=self.cleaned_data['modalidad'],
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                descripcion=self.cleaned_data['descripcion'],
                competencias=self.cleaned_data['competencias'],
                perfil_egreso=self.cleaned_data.get('perfil_egreso', ''),
                requisitos=self.cleaned_data.get('requisitos', ''),
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data.get('fecha_registro', '')
            )
            
            return nuevo_programa
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el instructor: {str(e)}")