usuarios = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'user123',
    'user3': 'user123'
}

print("Inicio de sesión")
usuario = input("Ingrese su nombre de usuario: ")
contrasenia = input("Ingrese su contraseña: ")
if usuario in usuarios:
    if usuarios.get(usuario) == contrasenia:
        print("Acceso Aprobado")
    else:
        print("Acceso Denegado")
else:
    print("Acceso Denegado")