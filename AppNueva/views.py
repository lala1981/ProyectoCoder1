from django.shortcuts import render
from AppNueva.models import Curso, Estudiantes
from django.http import HttpResponse
# Create your views here.

def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("Usuario creado exitosamente")
    
def guardar_estudiantes(request):
    estudiantes = Estudiantes(nombre="nombre", apellido="apellido", email="email")
    estudiantes.save()
    return 