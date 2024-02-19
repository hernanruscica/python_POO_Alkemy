def funciones_aritmeticas():
    accion = input('Ingrese una opción válida\nOpcion 1 : Sumar.\nOpcion 2 : restar\nOpcion 3: salir\n')
    while accion != '3':
        if accion == '1':
            valor01 = input('Ingrese el valor 1 que quiere sumar\n')
            valor02 = input('Ingrese el valor 2 que quiere sumar\n')
            suma = int(valor01) + int(valor02)
            print('La suma es = ', suma) 
        elif accion == '2':
            valor01 = input('Ingrese el valor 1 que quiere restar\n')
            valor02 = input('Ingrese el valor 2 que quiere restar\n')
            resta = int(valor01) - int(valor02)
            print('La resta es = ', resta) 
        else:
            print('Ingreso el valor:', accion, '. Dicha opción NO es VALIDA.\n')
        accion = input('Ingrese una opción válida\nOpcion 1 : Sumar.\nOpcion 2 : restar\nOpcion 3: salir\n')   
    print('Saliendo ...')
    
funciones_aritmeticas()