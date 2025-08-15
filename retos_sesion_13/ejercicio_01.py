print("Imprimimos los primeros 20 números de la sucesión de Lucas: ")
sucesion = []

for i in range(20):
    if i == 0:
        sucesion.append(2)
    elif i == 1:
        sucesion.append(1)
    else:
        sucesion.append(sucesion[i - 1] + sucesion[i - 2])

for numero in sucesion:
    print(numero, end=" ")

print() # Salto de línea final