from django.shortcuts import render
from . import models

# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo!")
def nosotros(request):
    return render(request, 'nosotros.html')

def articulos(request) :    
    models.Articulo.objects.create(precio = 2.5, nombre = 'voligoma3')
    articulo_precio = models.Articulo.objects.get(nombre='voligoma3').precio
    return HttpResponse(articulo_precio)

def crear_alumno(request, nombre, apellido, edad, nota_str):
    nota = float(nota_str)
    nuevo_estudiante = models.Estudiante.objects.create(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        nota=nota
    )
    # Retorna una respuesta con los detalles del estudiante creado
    return HttpResponse(f'Estudiante creado: {nuevo_estudiante.nombre} {nuevo_estudiante.apellido}, Edad: {nuevo_estudiante.edad}, Nota: {nuevo_estudiante.nota}')