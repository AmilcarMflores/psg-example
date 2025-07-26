while True:
    numero = int(input("Ingrese el número (o escriba '0' para terminar): "))
    if numero == 0:
         print("Programa finalizado.")
         break
    es_multiplo = numero % 7 == 0
    if es_multiplo:
        print(f'El número {numero} es múltiplo de 7')
    else: 
        print(f'El número {numero} no es múltiplo de 7')