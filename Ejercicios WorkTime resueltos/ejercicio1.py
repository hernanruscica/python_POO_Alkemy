
# Crear un algoritmo para calcular la sumatoria de los primeros cien
# números (del 01 al 100) con un ciclo while.
# - Guardar el algoritmo en un archivo llamado ejercicio1.py

hasta = 100
contador = 1
sumatoria = 0
while contador < hasta:
    sumatoria += contador
    contador += 1    
print('La sumatoria de los primeros ', hasta, 'numeros, es: ', sumatoria)
    