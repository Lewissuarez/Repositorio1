numero=[15,21,32,45]
for i in range(len(numero), 1, -1):
    if i % 3 == 0:
        numero.pop(i-1)

        print(numero)