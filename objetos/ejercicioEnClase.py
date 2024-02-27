"""
Enunciado
Cierta empresa requiere una aplicación informática 
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo. 

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""
from enum import Enum

class CatEmpleado(Enum):
    CAT1 = "Por Comision"
    CAT2 = "Salario Fijo"

class CatAntiguedad(Enum):
    CAT1 = 0
    CAT2 = 0.05
    CAT3 = 0.1

class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContratacion):
        self.__dni= dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__anioIngreso = anioIngreso
        self.__tipoContratacion = tipoContratacion
        self.__antiguedad = 2024 - anioIngreso
    def mostrarSalario(self):
        return print()
    
class PorComision:
    def __init__(self, salarioMinimo, clientesCaptados, MontoPorCliente):
        self.__salarioMinimo = salarioMinimo
        self.__clientesCaptados = clientesCaptados
        self.__MontoPorCliente = MontoPorCliente
    def mostrarSalario(self):
        #El salario = clientes captados * monto por cliente
        salarioComisiones = self.__clientesCaptados * self.__MontoPorCliente   
        if salarioComisiones > self.__salarioMinimo:
            return self.__salarioMinimo + salarioComisiones
        else:
            return self.__salarioMinimo

class SueldoFijo:
    def __init__(self, sueldoBasico, porcAdicional, antiguedad):
        self.__sueldoBasico = sueldoBasico
        self.__porcAdicional = porcAdicional
        self.__antiguedad = antiguedad
    def mostrarSalario(self):
        if self.__antiguedad.name == "CAT1":
            sueldo = self.__sueldoBasico
        elif self.__antiguedad.name == "CAT2":
            sueldo = self.__sueldoBasico + self.__sueldoBasico * 0.05
        else:
            sueldo = self.__sueldoBasico + self.__sueldoBasico * 0.1

    


        
            
        