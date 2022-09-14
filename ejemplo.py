clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        codigo = input('codigo de la fruta: ')
        nombre = input('nombre de la fruta: ')
        precio = input('precio: ')
        cliente = {'nombre':nombre, 'precio':precio}
        clientes[codigo] = cliente
    if opcion == '2':
        codigo = input('codigo de la fruta: ')
        if codigo in clientes:
            del clientes[codigo]
        else:
            print('No existe este codigo', codigo)
    if opcion == '3':
        codigo = input('codigo de la fruta: ')
        if codigo in clientes:
            print('codigo:', codigo)
            for clave, valor in clientes[codigo].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe este codigo', codigo)

    if opcion == '4':
        print("editar precio")
        codigo = input('codigo de la fruta: ')
        for codigo in range(len(clientes)):
            if cliente[precio] == codigo:
                precio[codigo] = int(input("nuevo precio: "))
        print("precio editado")


    if opcion == '5':
        print('Lista de frutas')
        for clave, valor in clientes.items():
            print(clave, valor ['nombre'])
    
    opcion = input('Menú de SuperMercado\n1 Comprar frutas\n2 Eliminar frutas\n3 Mostrar frutas\n4 Editar precio\n5 Lista de frutas\n6 Terminar\nElige una opción:')
