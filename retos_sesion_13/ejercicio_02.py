print("Imprimimos los 20 primeros números que sean múltiplos de 2 y 5: ")
lista = []
i = 1
contador = 0
while contador != 20:
    if i % 2 == 0 and i % 5 == 0:
        lista.append(i)
        contador += 1
    i += 1

for numero in lista:
    print(numero, end=" ")
