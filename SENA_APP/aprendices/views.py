from django.http import HttpResponse
from django.shortcuts import render
from .models import aprendiz
from django.template import loader


# Create your views here.
def aprendices(request):
    lista_aprendices = aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': lista_aprendices.count()
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())