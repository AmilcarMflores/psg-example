alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
print(alimentos)

# Añadimos 4 alimentos:
alimentos.update(
    pescado=["gato", "nutria"],
    trigo=["hamster", "canario"],
    leche=["gato", "perro"],
    semillas=["loro", "canario"]
)
print(alimentos)

# ¿Existe el alimento trigo?
existe_trigo = 'trigo' in alimentos
print(f"¿Existe 'trigo' en el diccionario? {existe_trigo}")

# Eliminamos la comida zanahoria:
zanahoria = alimentos.pop('zanahoria')
print(zanahoria, type(zanahoria))
print(alimentos)