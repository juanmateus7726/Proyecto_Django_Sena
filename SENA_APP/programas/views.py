from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Programa
from programas.forms import ProgramaForm
from django.views import generic
from django.views.generic import FormView

# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programa.html')
    
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    
    return HttpResponse(template.render(context, request))


class ProgramaFormView(FormView):
    template_name = 'crear_programa.html'
    form_class = ProgramaForm
    success_url = reverse_lazy('programas:lista_programas')
    
    def form_valid(self, form):
        nuevo_programa = form.save()
        return super().form_valid(form)
    
        messages.succes(
            Self.request,
            f'El programa {Programa.nombre} {Programa.apellido} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario'
        )
        print("Errores del formulario:", form.errors)
        return super().form_invalid(form)

