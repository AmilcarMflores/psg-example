prendas_deportivas = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
prendas_formales = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

set_deportivas = set(prendas_deportivas)
set_formales = set(prendas_formales)

# Unir ambos conjuntos
prendas_combinadas = set_deportivas.union(set_formales)

print(prendas_combinadas)