from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Proveedor

# Create your views here.
def test(request):
    proveedorUNO = Proveedor.objects.get(pk=1)
    #prueba = Producto.objects.create(nombre = "lamparita", precio = 100, stock_actual = 10, proveedor = proveedorUNO)
    prueba = Proveedor.objects.create(nombre = "Pedro", apellido = "Gonzalez", dni = 32456789)
    print(proveedorUNO)
    return HttpResponse(prueba.nombre)

def home(request):
    return render(request, 'home.html')
    #return HttpResponse('Root')

def new_supplier_form(request):
    return render(request, 'new_supplier_form.html')


def new_product_form(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'new_product_form.html', {'proveedores': proveedores})

def create_supplier(request):
    if request.method == 'POST':
        razon_social = request.POST.get('razon_social')
        cuit = request.POST.get('cuit')
        celular = request.POST.get('celular')

        # Crear instancia del proveedor y guardar en la base de datos
        proveedor = Proveedor(razon_social=razon_social, cuit=cuit, celular=celular)
        proveedor.save()    
        return redirect('suppliers')  
        #return HttpResponse('proveedor insertado en la BD')
    
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
        return redirect('products')
        #return HttpResponse('producto "%s" insertado en la BD' % producto.nombre)

def products(request):    
    print('ver todos los Products')
    products = Producto.objects.all()   
    #print(products[0].proveedor)
    return render(request, 'productos.html', {'productos': products})

def view_product(request, id):
    print('view product with id %d' % id)
    producto = Producto.objects.get(id=id)
    #print(producto.nombre)
    return render(request, 'view_products.html', {'producto': producto})
    #return HttpResponse('view product with id %d' % id)

def suppliers(request):
    print('ver todos los proveedores')
    proveedores = Proveedor.objects.all()   
    #return HttpResponse('suppliers')
    return render(request, 'proveedores.html', {'proveedores': proveedores})