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

def crear_alumno_form(request):
    return render(request, 'estudiante_crear.html')

def editar_alumno_form(request, id):         
    estudianteAeditar =  models.Estudiante.objects.get(id=id)
    return render(request, 'estudiante_editar.html', {'estudiante': estudianteAeditar})

def editar_alumno(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        id_estudiante = int(request.POST['id_estudiante'])
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = int(request.POST['edad'])
        nota = float(request.POST['nota'])

        # Actualizar el estudiante en la base de datos
        models.Estudiante.objects.filter(id=id_estudiante).update(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            nota=nota
        )

        # Obtener el estudiante actualizado
        estudiante_actualizado = models.Estudiante.objects.get(id=id_estudiante)
        print('Se actualizó el estudiante con id:', id_estudiante)

        # Renderizar la plantilla con el estudiante actualizado
        return render(request, 'estudiante_editado.html', {'estudiante': estudiante_actualizado})


def crear_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = int(request.POST['edad'])
        nota = float(request.POST['nota'])
    nuevo_estudiante = models.Estudiante.objects.create(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        nota=nota
    )        
    return render(request, 'estudiante_creado.html', {'nombre': nuevo_estudiante.nombre, 
                                                      'apellido': nuevo_estudiante.apellido, 
                                                      'edad': nuevo_estudiante.edad, 
                                                      'nota': nuevo_estudiante.nota})
def mostrar_alumnos(request):
    estudiantes_todos = models.Estudiante.objects.all()
    #print(estudiantes_todos[0].nombre)
    return render(request, 'estudiantes_mostrar_todos.html', {'estudiantes_todos': estudiantes_todos})

def mostrar_alumno(request, id):
    id = int(id)
    estudiante_encontrado = models.Estudiante.objects.get(id=id)
    print(estudiante_encontrado)
    return render(request, "estudiante_ver.html", {'estudiante': estudiante_encontrado})

from django.shortcuts import redirect
from . import models

def eliminar_alumno(request, id):
    # Convertir el ID a entero
    id = int(id)

    # Buscar el estudiante por su ID
    estudiante_a_eliminar = models.Estudiante.objects.get(id=id)

    # Eliminar el estudiante de la base de datos
    estudiante_a_eliminar.delete()

    # Redirigir a alguna página de confirmación o a donde desees
    return redirect('/showall')
