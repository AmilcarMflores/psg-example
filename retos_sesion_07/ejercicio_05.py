texto = input("Ingrese una cadena: ")

cadena_limpia = texto.replace(" ", "").lower() 

es_palindromo = cadena_limpia == cadena_limpia[::-1]

print(es_palindromo)