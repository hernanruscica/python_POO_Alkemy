# Crea una función llamada verificar_calificacion que reciba tres
# parámetros: nota1, nota2 y nota3
# ↪ Dentro de la función calcular el promedio de notas
# ↪ Si el promedio es mayor o igual a 6, entonces la función debe
# retornar un mensaje “Aprobado”, en caso contrario
# “Reprobado”
# ● Guardar en un archivo llamado ejercicio3.py


def verificar_calificacion(notas):
    nota_para_aprobar = 6
    sumatoria_notas = 0
    cantidad_notas = 0  
    for nota in notas:
        sumatoria_notas += nota
        cantidad_notas += 1

    promedio_notas = (sumatoria_notas / cantidad_notas)
    if promedio_notas >= nota_para_aprobar:
        return 'Aprobado'
    else:
        return 'Reprobado'

#Pruebas
notas_prueba = [6, 6, 6]
resultado = verificar_calificacion(notas_prueba)
print ('El estado del examen es:', resultado)