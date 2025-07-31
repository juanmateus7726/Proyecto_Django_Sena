from http.client import HTTPResponse
from django.template import loader
from django.shortcuts import render
from .models import Programa

# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HTTPResponse(template.render(context, request))