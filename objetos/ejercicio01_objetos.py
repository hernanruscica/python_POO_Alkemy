class producto:
    def __init__(self, id, nombre, decripcion, precio, foto):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = "Un grupo de niños son naufragos en un isla"
        self.__precio = precio
        self.__foto = foto
    #porcentaje en numeros enteros
    def actualizar_precio(self, porcentaje):
        self.__precio = self.__precio + self.__precio * (porcentaje / 100)
    def get_precio(self):
        return self.__precio
    def mostrar(self):
        print('Nombre: %s\nDescripcion: %s' % (self.__nombre, self.__descripcion))
        
    
libro = producto(1, 'Lord of the flies', 'descripcion', 8500, 'lordflies.jpg')

#print(libro.nombre, libro.get_precio())

libro.actualizar_precio(12)#aplica un aumento del 12%

print('Despues del aumento:', libro.get_precio())

libro.mostrar()