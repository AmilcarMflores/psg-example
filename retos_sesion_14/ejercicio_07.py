def crear_tablero():
    return [[' ' for columna in range(3)] for fila in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()

# Función para verificar ganador o empate
def ganador_empate(tablero):
    
    # Revisar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return f"Gana {tablero[i][0]}"
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return f"Gana {tablero[0][i]}"
    
    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return f"Gana {tablero[0][0]}"
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return f"Gana {tablero[0][2]}"
    
    # Revisar empate
    for fila in tablero:
        if ' ' in fila:
            return None
    return "Empate"

def tres_en_raya(tablero, jugador, fila, columna):
    if tablero[fila][columna] != ' ':
        print("Casilla ocupada, intenta de nuevo.")
        return False  # La jugada no se realizó
    tablero[fila][columna] = jugador
    return True  # La jugada se realizó

tablero = crear_tablero()
turno = 'X'

while True:
    mostrar_tablero(tablero)
    print(f"Juega: {turno}")

    # Pedir jugada
    fila = int(input("Fila (0-2): "))
    columna = int(input("Columna (0-2): "))

    if tres_en_raya(tablero, turno, fila, columna):
        resultado = ganador_empate(tablero)
        if resultado:
            mostrar_tablero(tablero)
            print(resultado)
            break
        # Cambiar turno
        turno = 'O' if turno == 'X' else 'X'

