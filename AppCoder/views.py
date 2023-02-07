from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estudiante
# Create your views here.


def inicio(request):
    return HttpResponse("Hola, bienvenido a mi pagina")


def add_estud(request):
    est = Estudiante(nombre="pepe", apellido="Perez",
                     correo="a@a.com")
    est.save()

    return HttpResponse("Se agrego un nuevo estudiante.")
