edad = int(input("Ingrese la edad del cliente: "))
monto_compra = float(input("Ingrese el monto de la compra: "))

if edad > 60 and monto_compra > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and monto_compra > 500:
    descuento = 0.10
else:
    descuento = 0.02

monto_descuento = monto_compra * descuento
monto_final = monto_compra - monto_descuento

print(f"Descuento aplicado: {descuento * 100}%")
print(f"Monto con descuento: {monto_final}")
