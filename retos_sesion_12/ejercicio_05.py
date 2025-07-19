nombre = input("Nombre: ")
telefono = input("Teléfono: ")

if nombre and telefono.startswith('+') and len(telefono) == 12 and telefono[1:].isdigit():
    print("-------------")
    print("Contacto guardado")
else:
    print("-------------")
    print("Datos incorrectos")
