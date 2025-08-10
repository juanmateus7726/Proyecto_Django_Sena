from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import instructor

# Create your views here.

def instructores(request):
    lista_instructores = instructor.objects.all().order_by('apellido', 'nombre')
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_instructor(request, instructor_id):
    inst = get_object_or_404(instructor, id=instructor_id)
    cursos_coordinados = inst.cursos_coordinados.all()
    cursos_impartidos = inst.cursos_impartidos.all()
    template = loader.get_template('detalle_instructor.html')
    
    context = {
        'instructor': inst,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos
    }
    
    return HttpResponse(template.render(context, request))