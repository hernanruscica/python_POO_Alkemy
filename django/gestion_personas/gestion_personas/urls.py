"""
URL configuration for gestion_personas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Importa 'include'
from landing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_mundo, name="hola_mundo"),
    path('landing/', include('landing.urls')),
    path('createform/', views.crear_alumno_form, name="crear_alumno_form"),
    path('create/', views.crear_alumno, name='crear_alumno'),
    path('showall/', views.mostrar_alumnos, name="mostrar_alumnos"),
    path('showbyid/<int:id>', views.mostrar_alumno, name =  "mostrar_alumno"),
    path('editform/<int:id>', views.editar_alumno_form, name =  "editar_alumno_form"),
    path('edit/', views.editar_alumno, name="editar_alumno"),
    path('delete/<int:id>', views.eliminar_alumno, name="eliminar_alumno"),    
    path('saludardos/', views.saludar_clase12, name="saludar_clase12")
]
