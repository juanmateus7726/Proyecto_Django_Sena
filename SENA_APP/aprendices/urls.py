from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aprendices/', views.aprendices, name='lista_aprendices')
]