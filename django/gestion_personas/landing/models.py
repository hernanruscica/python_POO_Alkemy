from django.db import models

# Create your models here.
class Articulo(models.Model):
    precio = models.FloatField()
    nombre = models.CharField(max_length = 45)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    nota = models.FloatField()