while True:
    frase = input("Ingrese la frase (o escriba 'salir' para terminar): ")
    
    if "salir" in frase.lower():
        print("Programa finalizado.")
        break
    
    frase_limpia = frase.lower().replace(" ", "")
    es_palindromo = frase_limpia == frase_limpia[::-1]

    if es_palindromo:
        print(f'La frase "{frase}" es un palíndromo.')
    else:
        print(f'La frase "{frase}" no es un palíndromo.')
