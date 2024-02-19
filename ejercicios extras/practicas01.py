frutas = ['Naranja', 'Limon', 'Mandarina', 'Banana', 'Uva', 'Ciruela', 'Pera', 'Durazno', 'pelón', 'Sandia', 'Ananá', 'Manzana', 'Cereza', 'Frutilla']
print(type(frutas)) #<class 'list'>

#metodos de las listas
codigos_frutas_pares = []
codigos_frutas_impares = []
codigos_frutas = []

#append()
for i in range(2, 21,2):
    codigos_frutas_pares.append(i)

#insert() en la posicion 0 (queda ordenado de may a men)
for i in range(1, 20,2):
    codigos_frutas_impares.insert(0, i)

codigos_frutas_impares.reverse()

print(codigos_frutas_pares, codigos_frutas_impares)

codigos_frutas.extend(codigos_frutas_pares)
codigos_frutas.extend(codigos_frutas_impares)

print(codigos_frutas)

#sort()
codigos_frutas.sort()


print(codigos_frutas)
#count()
cantidad_frutas = len(frutas)
cantidad_codigos_frutas = len(codigos_frutas)
for i in range(cantidad_frutas , cantidad_codigos_frutas):
    codigos_frutas.remove(i + 1)

print(codigos_frutas)

#index
fruta_buscada = 'Durazno'
fruta_reemplazo = 'Melocotón'
pos_fruta_buscada = frutas.index(fruta_buscada)

print(fruta_buscada, frutas)

#pop
fruta_sacada = frutas.pop(pos_fruta_buscada)

#insert
frutas.insert(pos_fruta_buscada, fruta_reemplazo)
print(fruta_buscada, frutas)