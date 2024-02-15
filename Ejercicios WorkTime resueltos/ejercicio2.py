# Crear una lista con 5 elementos y luego aplica los siguientes
# accionables:
# ↪ Imprimir el último elemento
# ↪ Modificar el valor del tercer elemento
# ↪ Agregar dos elementos
# ↪ Eliminar algún elemento
# ● Guardar en un archivo llamado ejercicio2.py
fruta_3 = 'naranja'
mi_lista = ['banana', 'pera', 'mandarina', 'durazno', 'ciruela', 'sandia', 'frutilla', fruta_3]
print('La ultima fruta es:', mi_lista[-1])
fruta_temp = mi_lista[2]
mi_lista[2] = fruta_3
mi_lista[-1] = fruta_temp
print('El orden de las frutas es:', mi_lista)
mi_lista.insert(0, 'anana')
mi_lista.append('quinoto')
mi_lista.remove('sandia')
print('Las nueva lista de frutas es:', mi_lista)