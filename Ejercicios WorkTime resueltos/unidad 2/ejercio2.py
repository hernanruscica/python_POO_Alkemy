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
    
pichichuz = Perro(4, TipoAnimal.VERTEBRADO, "Pichichuz", "callejero")


    
