# Cinco funciones (métodos de cadenas)

# 1. partition()
texto = "python es divertido"
resultado = texto.partition("es")
print(resultado)  # ('python ', 'es', ' divertido')

# 2. zfill()
numero = "42"
rellenado = numero.zfill(5)
print(rellenado)  # 00042

# 3. removeprefix()
ruta = "/home/usuario"
print(ruta.removeprefix("/home/"))  # usuario

# 4. expandtabs()
texto_tabulado = "Python\tes\tgenial"
sin_tab = texto_tabulado.expandtabs(4)
print(sin_tab)  # Python  es  genial

# 5. rjust()
palabra = "Hola"
alineado = palabra.rjust(10, "-")
print(alineado)  # ------Hola