''' SkyRoute - Sistema de Gestión de Pasajes Aéreos
    Proyecto ABP - Evidencia 2
    Integrantes del grupo:
        Milton Amaya, DNI:30.310.864
        Otto Acosta, DNI:46.227.388
        Jesica Elizabeth Amaya, DNI:27.660.701
        Shunko Rodriguez, DNI:30.151.105
        Rocío Belén Issetta, DNI:39.172.315
        Torres Álvaro Matías, DNI:44.037.240
        
    Cómo ejecutar:
        Abrir terminal y correr: python main.py
'''
#Variable multilineas del menu principal
menu='''
        Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes
        ------------------------------------------------------
        1. Gestionar Clientes
        2. Gestionar Destinos
        3. Gestionar Ventas
        4. Consultar Ventas
        5. Botón de Arrepentimiento
        6. Ver Reporte General
        7. Acerca del Sistema
        8. Salir       
        '''
#Variable multilinea submenu de Gestionar Clientes
submenu_clientes='''
        -- GESTIONAR CLIENTES --
        1. Ver Clientes
        2. Agregar Cliente
        3. Modificar Cliente
        4. Eliminar Cliente
        5. Volver al Menú Principal
        '''
#Variable multilinea submenu de Gestionar Destinos
submenu_destinos='''
        -- GESTIONAR DESTINOS --
        1. Ver Destinos
        2. Agregar Destino
        3. Modificar Destino
        4. Eliminar Destino
        5. Volver al Menú Principal
        '''
#Variable multilinea submenu de COnsultar ventas
submenu_consultas='''
        -- GESTIONAR CONSULTA DE VENTAS --
        1. Ver todas las ventas
        2. Ventas mas vendidas
        3. Ventas de la última semana
        4. Ventas por año
        5. Ver ventas por destino
        6. Volver al Menú Principal
        '''
#comienzo del menu principal
while True:
    print(menu)	#muestra la variable menu
    opcion=int(input('	Seleccione una opción: '))	#pide opcion del menu principal
    
    #Condicionales de acuerdo a la opcion seleccionada
    if opcion == 1:
        while True:	#ciclo del submenu gestion clientes
            print(submenu_clientes)	#muestra la variable del submenu de clientes
            opcion = int(input('	Seleccione una opción: '))	#pide opcion del submenu clientes
            
            #Condicionales de acuerdo a la opcion seleccionada del submenu
            if opcion == 1:
                print('Mostrando lista de clientes...')
            elif opcion == 2:	#en caso de seleccionar agregar un cliente pedimos datos
                razon_social = input('Ingrese razón social: ')
                cuit = input('Ingrese CUIT: ')
                correo = input('Ingrese correo de contacto: ')
                print('Se guardó el cliente: ',razon_social, ' CUIT:',cuit,' Email:',correo)
            elif opcion == 3:
                print('Modificar datos del cliente...')
            elif opcion == 4:
                print('Eliminar un cliente...')
            elif opcion == 5:	#cuando se selecciono la opcion 5 sale del submenu
                break
            else:
                print('Opción inválida!')	#en caso de seleccionar cualquier numero, da aviso
            
    elif opcion == 2:
        while True:	#ciclo del submenu gestion destinos
            print(submenu_destinos)	#muestra la variable del submenu de gestionar destinos
            opcion = int(input('	Seleccione una opción: '))

            if opcion == 1:
                print('Mostrando destinos disponibles...')
            elif opcion == 2:
                print('Agregar un destino nuevo...')
            elif opcion == 3:
                print('Modificar un destino...')
            elif opcion == 4:
                print('Eliminar un destino...')
            elif opcion == 5:	#cuando se selecciono la opcion 5 sale del submenu
                break
            else:
                print('Opción inválida.')	#en caso de seleccionar cualquier numero, da aviso
    elif opcion == 3:
        print('Ingresó a la Gestión de Ventas...')
    elif opcion == 4:
        while True:	#ciclo del submenu Consulta Ventas
            print(submenu_consultas)	#muestra la variable del submenu de consulta de ventas
            opcion = int(input('	Seleccione una opción: '))

            if opcion == 1:
                print('Mostrando todas las ventas...')
            elif opcion == 2:
                print('Mostrando las ventas mas vendidas...')
            elif opcion == 3:
                print('Mostrando las ventas de la última semana...')
            elif opcion == 4:
                print('Mostrando las ventas por año...')
            elif opcion == 5:
                print('Mostrando las ventas por destino...')
            elif opcion == 6:	#cuando se selecciono la opcion 6 sale del submenu
                break
            else:
                print('Opción inválida.')	#en caso de seleccionar cualquier numero, da aviso
    elif opcion == 5:
         print('Accediendo al Botón de Arrepentimiento...')
    elif opcion == 6:
         print('Mostrando Reporte General...')
    elif opcion == 7:
         print('Sistema creado por estudiantes de TSCDeIA 2025. v1.r0')
    elif opcion == 8:
         print('Gracias por utilizar SkyRoute. ¡Hasta pronto!')
         break
    else:
         print('Opción inválida. Intente nuevamente.')	#en caso de seleccionar cualquier numero, da aviso
#FIn del programa
