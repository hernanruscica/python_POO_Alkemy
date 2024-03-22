from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def test(request):
    prueba = models.Proveedor.objects.create(nombre = "pepe", apellido = "lui", dni = 25478965)
    return HttpResponse(prueba.nombre)

def root(request):
    return HttpResponse('Root')