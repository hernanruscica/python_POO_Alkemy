from django.shortcuts import render
from . import models

# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo!")
def nosotros(request):
    return render(request, 'nosotros.html')

def articulos(request) :
    models.Articulo.objects.create(precio = 1.5, nombre = 'voligoma')
    articulo_precio = models.Articulo.objects.get(nombre='voligoma').precio
    return HttpResponse(articulo_precio)

