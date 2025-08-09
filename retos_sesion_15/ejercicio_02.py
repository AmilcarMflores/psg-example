class FrutaNoPermitidaError(Exception):
    pass

def canasta_frutas():
    frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
    canasta = []

    while True:
        fruta = input("Ingrese una fruta (o 'salir' para terminar): ")
        if fruta.lower() == "salir":
            break
        try:
            if fruta not in frutas_permitidas:
                raise FrutaNoPermitidaError(f"'{fruta}' no es una fruta permitida")
        except FrutaNoPermitidaError as e:
            print(e)
        else:
            canasta.append(fruta)
            print("Fruta agregada con éxito")
        finally:
            print(f"Canasta actual: {canasta}\n")

    print("Canasta final:", canasta)

canasta_frutas()