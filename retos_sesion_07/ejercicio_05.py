texto = "Hola"
cadena_limpia = texto.replace(" ", "").lower() 
# Verificar si es palíndromo
comparar = cadena_limpia == cadena_limpia[::-1]
print(comparar)  # Salida: True
