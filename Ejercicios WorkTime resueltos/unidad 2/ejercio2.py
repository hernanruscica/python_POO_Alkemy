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
    
class Perro(Animal):
    def __init__(self, cant_patas, tipo_animal, nombre, raza):
        super().__init__(cant_patas, tipo_animal)
        self.__nombre = nombre
        self.__raza = raza
    def correr(self):
        return "estoy corriendo"

class Aguila(Animal):
    def __init__(self, cant_patas, tipo_animal, nombre, raza):
        super().__init__(cant_patas, tipo_animal)
        self.__nombre = nombre
        self.__raza = raza
    def volar(self)        :
        return print('Me llamo %s y estoy volando...' % self.__nombre)
    
pichichuz = Perro(4, TipoAnimal.VERTEBRADO, "Pichichuz", "callejero")

aguilardo = Aguila(2, TipoAnimal.VERTEBRADO, "Aguilardo", "aguila calva")

print(pichichuz.comer())

aguilardo.volar()
    
