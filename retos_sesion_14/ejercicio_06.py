def separar_pares_impares(lista_numeros):
    pares = []
    impares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

numeros = [10, 15, 22, 33, 40, 51, 60]
pares, impares = separar_pares_impares(numeros)

print("Lista de números: ", numeros)
print("Números pares:", pares)
print("Números impares:", impares)
