from django.db import models

# Create your models here.
class Proveedor(models.Model):
    razon_social = models.CharField(max_length = 45)
    cuit = models.CharField(max_length = 45) 
    celular = models.CharField(max_length = 45) 
    def __str__(self):
        return self.razon_social
    

class Producto(models.Model):
    nombre = models.CharField(max_length = 45)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre

