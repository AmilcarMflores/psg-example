productos = ["Oreo", "Bon Bon Bum", "Chizitos", "Trencito", "Galletas Marias"]
precios = [2.5, 0.5, 1.0, 1.8, 1.2]
print(productos)
print(precios)

# 1. Agregar 2 productos nuevos al final
productos.extend(["Snickers", "M&M's"])
precios.extend([2.8, 2.3])
print(productos)
print(precios)

# 2. Eliminar el producto "Bon Bon Bum"
index = productos.index("Bon Bon Bum")
productos.pop(index)
precios.pop(index)
print(productos)
print(precios)

# 3. ¿Cuánto cuesta "Oreo" y "Chizitos"?
precio_oreo = precios[productos.index("Oreo")]
precio_chizitos = precios[productos.index("Chizitos")]
print("Precio de Oreo:", precio_oreo)
print("Precio de Chizitos:", precio_chizitos)

# 4. Producto más caro y más barato
indice_max = precios.index(max(precios))
indice_min = precios.index(min(precios))
print("Producto más caro:", productos[indice_max], "->", precios[indice_max])
print("Producto más barato:", productos[indice_min], "->", precios[indice_min])

# 5. ¿Cuántos productos hay?
print("Cantidad total de productos:", len(productos))

# 6. ¿Cuánto cuestan todos los productos?
print("Costo total:", sum(precios))

# 7. Ordenar de más barato a más caro (Este se me complicó, tuve que usar sorted, zip y lista por comprensión)
productos_ordenados = [x for _, x in sorted(zip(precios, productos))]
precios_ordenados = sorted(precios)
print("Productos ordenados de más barato a más caro:")
print(productos_ordenados)
print(precios_ordenados)

# 8. Eliminar todos los productos
productos.clear()
precios.clear()
print("Listas vacías:", productos, precios)
