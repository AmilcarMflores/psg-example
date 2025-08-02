def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

texto = "Hola mundooo"
resultado = contar_vocales(texto)
print(f"La cantidad de vocales en '{texto}' es: {resultado}")
