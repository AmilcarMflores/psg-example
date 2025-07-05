tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

set_fisica = set(tienda_fisica)
set_online = set(tienda_online)

# a. Clientes que compraron en ambos canales
ambos_canales = set_fisica & set_online
print("a. Compraron en ambos canales:", ambos_canales)

# b. Clientes que compraron solo en la tienda física 
solo_fisica = set_fisica - set_online
print("b. Compraron solo en la tienda física:", solo_fisica)

# c. Clientes que compraron solo online
solo_online = set_online - set_fisica
print("c. Compraron solo online:", solo_online)