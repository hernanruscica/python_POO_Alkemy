from django.db import models

# Create your models here.
class Articulo(models.Model):
    precio = models.FloatField()
    nombre = models.CharField(max_length = 45)

