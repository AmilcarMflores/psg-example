print("Tarjeta y Huella (XOR)")
tarjeta = True
huella = True
print(tarjeta, "xor", huella, "=", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = True
huella = False
print(tarjeta, "xor", huella, "=", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = False
huella = True
print(tarjeta, "xor", huella, "=", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = False
huella = False
print(tarjeta, "xor", huella, "=", (tarjeta or huella) and not (tarjeta and huella))
