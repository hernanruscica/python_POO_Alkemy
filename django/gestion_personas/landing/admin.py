from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad', 'nota']
    search_fields = ['apellido']


# Register your models here.

admin.site.register(Estudiante, EstudianteAdmin)