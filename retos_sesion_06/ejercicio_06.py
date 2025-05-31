N = 300 ** 3  # Calcula el cubo de 300
rango_inferior = 0
rango_superior = 27_000_000

en_rango = (N > rango_inferior) and (N < rango_superior)

print("El cubo de 300 es:", N)
print("¿Está el cubo de 300 en el rango (0, 27,000,000)?", en_rango)