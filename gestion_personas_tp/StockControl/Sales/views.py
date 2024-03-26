from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Proveedor

# Create your views here.
def test(request):
    proveedorUNO = Proveedor.objects.get(pk=1)
    #prueba = Producto.objects.create(nombre = "lamparita", precio = 100, stock_actual = 10, proveedor = proveedorUNO)
    prueba = Proveedor.objects.create(nombre = "Pedro", apellido = "Gonzalez", dni = 32456789)
    return HttpResponse(prueba.nombre)

def root(request):
    return HttpResponse('Root')

def new_supplier_form(request):
    return render(request, 'new_supplier_form.html')


def new_product_form(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'new_product_form.html', {'proveedores': proveedores})

def create_supplier(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        # Crear instancia del proveedor y guardar en la base de datos
        proveedor = Proveedor(nombre=nombre, apellido=apellido, dni=dni)
        proveedor.save()      
        return HttpResponse('proveedor insertado en la BD')
    
def create_product(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock')
        proveedor_id = request.POST.get('proveedor')
        #print(proveedor_id)
        proveedor = Proveedor.objects.get(id = proveedor_id)
        #print(proveedor.nombre)
        producto = Producto(nombre = nombre, precio = precio, stock_actual = stock_actual, proveedor = proveedor)
        producto.save()
        return HttpResponse('producto "%s" insertado en la BD' % producto.nombre)

def products(request):    
    print('ver todos los Products')
    products = Producto.objects.all()   
    return render(request, 'productos.html', {'productos': products})
def suppliers(request):
    return HttpResponse('suppliers')