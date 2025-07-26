print("Tablero de ajedrez de 8x8 con # y *:")
for i in range(8):
    fila = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            fila += "# "
        else:
            fila += "* "
    print(fila)
