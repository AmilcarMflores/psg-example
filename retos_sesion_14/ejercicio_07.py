# Tablero vacío 3x3
tablero = [[" " for _ in range(3)] for _ in range(3)]
turno_actual = "X"
juego_terminado = False

def mostrar_tablero():
    for fila in tablero:
        print(fila)
    print()

def verificar_ganador():
    # Filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

def tablero_lleno():
    for fila in tablero:
        if " " in fila:
            return False
    return True

def tres_en_raya_interactivo():
    global turno_actual, juego_terminado
    mostrar_tablero()

    while not juego_terminado:
        print(f"Turno de {turno_actual}")
        try:
            fila = int(input("Ingresa la fila (0 a 2): "))
            columna = int(input("Ingresa la columna (0 a 2): "))
        except ValueError:
            print("Ingresa solo números enteros.")
            continue

        if not (0 <= fila <= 2 and 0 <= columna <= 2):
            print("Posición fuera del tablero. Usa valores de 0 a 2.")
            continue

        if tablero[fila][columna] != " ":
            print("Casilla ocupada. Elige otra.")
            continue

        tablero[fila][columna] = turno_actual
        mostrar_tablero()

        ganador = verificar_ganador()
        if ganador:
            print(f"Jugador {ganador} ha ganado!")
            juego_terminado = True
            break
        elif tablero_lleno():
            print("Empate!")
            juego_terminado = True
            break

        # Cambiar de turno
        turno_actual = "O" if turno_actual == "X" else "X"

tres_en_raya_interactivo()
