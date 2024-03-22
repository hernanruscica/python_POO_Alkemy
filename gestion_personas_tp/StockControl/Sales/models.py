from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length = 45)
    apellido = models.CharField(max_length = 45) 
    dni = models.PositiveIntegerField()

class Producto(models.Model):
    nombre = models.CharField(max_length = 45)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)


