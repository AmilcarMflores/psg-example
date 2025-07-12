arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,  
    "🦒": 1
}
print(arca)

# Añadimos al arca 3 especies más:
arca.update({
    "🐍": 2,
    "🦅": 2,
    "🐢": 2
})
print(arca)

# Tomamos lista de los animales:
print("Lista de los animales en el arca:")
iterador = iter(arca.items())
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

# ¿Existe en el arca la especie dragon 🐲?
existe_dragon = "🐲" in arca
print(f"¿Existe dragón en el arca? -> {existe_dragon}")

# Eliminamos la especie unicornio del arca:
arca.pop("🦄")
print(arca)

# Modificamos la especie jirafa por 2:
arca.update({"🦒": 2})
print(arca)

# Vaciar el arca después del diluvio
arca.clear()
print(arca)