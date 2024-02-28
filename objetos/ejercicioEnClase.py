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
        pass
    
class PorComision(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContratacion, salarioMinimo, clientesCaptados, MontoPorCliente):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContratacion)
        self.__salarioMinimo = salarioMinimo
        self.__clientesCaptados = clientesCaptados
        self.__MontoPorCliente = MontoPorCliente
    def mostrarSalario(self):
        #El salario = clientes captados * monto por cliente
        salarioComisiones = self.__clientesCaptados * self.__MontoPorCliente
        if salarioComisiones > self.__salarioMinimo:
            salarioAcobrar = salarioComisiones
        else:
            salarioAcobrar = self.__salarioMinimo
        return print('******\nNombre y apellido: %s %s\nSalario a cobrar: %.2f (%s)\n******\n ' % (self._Empleado__nombre, self._Empleado__apellido, salarioAcobrar, self._Empleado__tipoContratacion.value))

class PorSueldoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContratacion, sueldoBasico, porcAdicional):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContratacion)
        self.__sueldoBasico = sueldoBasico
        self.__porcAdicional = porcAdicional
        self.__antiguedad = 2024 - anioIngreso
    def mostrarSalario(self):         
        sueldo = self.__sueldoBasico + self.__sueldoBasico * self.__porcAdicional.value
        return print('******\nNombre y apellido: %s %s\nSalario a cobrar: %.2f (%s)\n******\n ' % (self._Empleado__nombre, self._Empleado__apellido, sueldo, self._Empleado__tipoContratacion.value))
        

    
empleadoPorComision01 = PorComision("33222111", "Matias", "Lopez", 2018, CatEmpleado.CAT1, 350, 1, 14)
print(empleadoPorComision01.mostrarSalario())

empleadoPorSueldoFijo01 = PorSueldoFijo("11222333", "Juan", "Flores", 2005, CatEmpleado.CAT2, 400, CatAntiguedad.CAT3)
print(empleadoPorSueldoFijo01.mostrarSalario())
            
        