productos = ["Oreo", "Bon Bon Bum", "Chizitos", "Trencito", "Galletas Marias"]
precios = [3.5, 1.5, 2.0, 3.0, 2.5]

print("Productos iniciales:", productos)
print("Precios iniciales:", precios)

# 1. Agregar 2 productos nuevos al final
productos.extend(["Snickers", "M&M's"])
precios.extend([5.0, 4.5])
print("\nDespués de agregar productos:")
print(productos)
print(precios)

# 2. Eliminar el producto "Bon Bon Bum"
indice_bonbon = productos.index("Bon Bon Bum")
productos.pop(indice_bonbon)
precios.pop(indice_bonbon)
print("\nDespués de eliminar 'Bon Bon Bum':")
print(productos)
print(precios)

# 3. ¿Cuánto cuesta "Oreo" y "Chizitos"?
precio_oreo = precios[productos.index("Oreo")]
precio_chizitos = precios[productos.index("Chizitos")]
print("\nPrecio de Oreo:", precio_oreo)
print("Precio de Chizitos:", precio_chizitos)

# 4. Producto más caro y más barato
indice_max = precios.index(max(precios))
indice_min = precios.index(min(precios))
print("\nProducto más caro:", productos[indice_max], "->", precios[indice_max])
print("Producto más barato:", productos[indice_min], "->", precios[indice_min])

# 5. ¿Cuántos productos hay?
print("\nCantidad total de productos:", len(productos))

# 6. ¿Cuánto cuestan todos los productos?
print("Costo total:", sum(precios))

# 7. Ordenar de más barato a más caro usando nombres descriptivos
productos_ordenados = [producto for precio, producto in sorted(zip(precios, productos))]
precios_ordenados = sorted(precios)
print("\nProductos ordenados de más barato a más caro:")
print(productos_ordenados)
print(precios_ordenados)

# 8. Eliminar todos los productos
productos.clear()
precios.clear()
print("\nListas vacías:", productos, precios)
