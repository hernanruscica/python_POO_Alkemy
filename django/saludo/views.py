from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from . import views

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo!")

def mostrar_nombre(request):
    nombre = 'Cesar Hernan Ruscica'  # Puedes cambiar esto por tu nombre
    return render(request, 'mostrar_nombre.html', {'nombre': nombre})


