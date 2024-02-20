class producto:
    def __init__(self, id, nombre, decripcion, precio, foto):
        self.id = id
        self.nombre = nombre
        self.descripcion = decripcion
        self.precio = precio
        self.foto = foto
    #porcentaje en numeros enteros
    def actualizar_precio(self, porcentaje):
        self.precio = self.precio + self.precio * (porcentaje / 100)
    def get_precio(self):
        return self.precio
        
    
libro = producto(1, 'Lord of the flies', 'descripcion', 8500, 'lordflies.jpg')

print(libro.nombre, libro.precio)

libro.actualizar_precio(12)

print('Despues del aumento:', libro.precio)