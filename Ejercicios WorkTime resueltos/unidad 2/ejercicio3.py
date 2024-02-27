
# “Juan Lopez tiene 25 años y es de profesión Abogado. Por la
# tarde, después de trabajar, sale a caminar. También tiene una
# bicicleta amarilla marca “Massino” y a veces sale a dar
# vueltas en ella”.

from enum import Enum

class profesiones(Enum):
    ABOGADO = 0
    CONTADO = 1
    PROGRAMADOR = 3

class persona:
    def __init__(self, nombre, apellido, edad, profesion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__profesion = profesion
    def mostrar(self):
        return print('Soy %s %s, mi profesion es %s y tengo %d años.' % (self.__nombre, self.__apellido, self.__profesion.name, self.__edad))
    def trabajar(self):
        return print('Soy %s %s, tengo %d y estoy trabajando de %s'  % (self.__nombre, self.__apellido, self.__edad, self.__profesion.name))
    def caminar(self):
        return print('Soy %s %s y estoy caminado ...'  % (self.__nombre, self.__apellido))
class bicicleta:
    def __init__(self, marca, color, duenio):
        self.__marca = marca
        self.__color = color
        self.__duenio = duenio
    def dar_vueltas(self):
        return print ('soy la bicicleta de %s marca "%s" de color %s y estoy dando vueltas' % (self.__duenio, self.__marca, self.__color))

abogado_juan_lopez = persona('Juan', 'Lopez', 43, profesiones.ABOGADO)
bicicleta_Massino_amarilla = bicicleta('Massino', 'Amarilla', 'Juan Lopez')

abogado_juan_lopez.trabajar()
abogado_juan_lopez.caminar()
bicicleta_Massino_amarilla.dar_vueltas()