from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso


# Create your views here.

def crea_curso (self):

    curso = Curso(nombre='Javascript', camada=12343)
    curso.save()
    documento = f'Se creó el curso {curso.nombre} con el número de camada {curso.camada}'
    return HttpResponse (documento)


