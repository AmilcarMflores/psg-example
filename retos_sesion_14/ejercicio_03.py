def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

n = 5
indice = n - 1  # porque lucas(0) es el 1er número
print(f"El {n}º número de la sucesión de Lucas es: {lucas(indice)}")
