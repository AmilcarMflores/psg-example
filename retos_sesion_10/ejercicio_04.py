jane_postres = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
john_postres = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

postres_comunes = jane_postres & john_postres
total_unicos = len(jane_postres | john_postres)

# Porcentaje de compatibilidad
porcentaje = (len(postres_comunes) / total_unicos * 100)
es_compatible = porcentaje > 50

# Resultado
print(f"Postres en común: {postres_comunes}, {len(postres_comunes)} coincidencias")
print(f"Porcentaje de compatibilidad: {porcentaje}%")
print(f"¿Son compatibles?", "Sí" * es_compatible + "No" * (not es_compatible))