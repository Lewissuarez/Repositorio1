


from re import I


clientes = {}
opcion = ''
while opcion != '5':
    if opcion == '1':
        nombre = input('nombre de la fruta: ')
        color =  input('color de la fruta: ')
        precio = input('precio: ')
        cliente = {'nombre':nombre, 'precio':precio}
        clientes[nombre] = cliente
    
    if opcion == '2':
        print('Lista de frutas')
        for clave, valor in clientes.items():
            print(clave)
    
    opcion = input('Menú Salpicon\n1 añadir frutas\n2 lista de frutas\nElige una opción:')



