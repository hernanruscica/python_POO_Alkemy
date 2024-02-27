from enum import Enum

class TipoAnimal(Enum):
    VERTEBRADO = 1
    INVERTEBRADO = 2

class Animal:
    def __init__(self, cant_patas, tipo_animal ):
        self.__cantidad_patas = cant_patas
        self.__vertebrado = tipo_animal
    def comer(self):
        return "estoy comiendo"
    def emitir_sonido(self):
        return print("estoy emitiendo mi sonido caracteristico ")
    
class Perro(Animal):
    def __init__(self, cant_patas, tipo_animal, nombre, raza):
        super().__init__(cant_patas, tipo_animal)
        self.__nombre = nombre
        self.__raza = raza
    def correr(self):
        return "estoy corriendo"
<<<<<<< HEAD
=======
    def emitir_sonido(self):
        return print("Soy %s y estoy ladrando" % self.__nombre)
>>>>>>> 162aa22955ad1b3fb24abe0347cfb42bc9f2f7c7

class Aguila(Animal):
    def __init__(self, cant_patas, tipo_animal, nombre, raza):
        super().__init__(cant_patas, tipo_animal)
<<<<<<< HEAD
        self.__nombre = nombre
        self.__raza = raza
    def volar(self)        :
        return print('Me llamo %s y estoy volando...' % self.__nombre)
=======
        self.__nombre= nombre
        self.__raza = raza
    def volar(self):        
        mensaje = print("%s dice: 'estoy volando'" % self.__nombre)
        return mensaje
    
        
            
>>>>>>> 162aa22955ad1b3fb24abe0347cfb42bc9f2f7c7
    
pichichuz = Perro(4, TipoAnimal.VERTEBRADO, "Pichichuz", "callejero")
Ricardo = Aguila(2, TipoAnimal.VERTEBRADO, "Ricardo", "Ave")
#print(pichichuz.correr())    
Ricardo.volar()
pichichuz.emitir_sonido()
Ricardo.emitir_sonido()

<<<<<<< HEAD
aguilardo = Aguila(2, TipoAnimal.VERTEBRADO, "Aguilardo", "aguila calva")

print(pichichuz.comer())

aguilardo.volar()
    
=======
>>>>>>> 162aa22955ad1b3fb24abe0347cfb42bc9f2f7c7
