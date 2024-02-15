def funciones_aritmeticas():
    accion = input('opcion 1 : Sumar - opcion 2 : restar - opcion 3: salir' )
    while accion != 3:
        if accion == 1:
            valor01 = input('Ingrese el valor 1 que quiere sumar')
            valor02 = input('Ingrese el valor 2 que quiere sumar')
            print('La suma es = ', valor01 + valor02) 
        else:
            valor01 = input('Ingrese el valor 1 que quiere sumar')
            valor02 = input('Ingrese el valor 2 que quiere sumar')
            print('La resta es = ', valor01 - valor02) 
        accion = input('opcion 1 : Sumar - opcion 2 : restar - opcion 3: salir' )
    
    
    
funciones_aritmeticas()