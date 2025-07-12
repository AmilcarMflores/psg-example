# Hábitats en peligro de extinción
habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}
print(habitats)

# Añadimos 2 habitats con 2 especies cada uno:
habitats.update({
    "sabana africana": {
        "especies": {"león", "elefante"}
    },
    "arrecife de coral": {
        "especies": {"tortuga marina", "pez payaso"}
    }
})
print(habitats)

# ¿Existe el habitat amazonas?
existe_amazonas = "amazonas" in habitats
print(f"¿Existe el hábitat amazonas? {existe_amazonas}")

# Añadimos al amazonas la especie anaconda:
habitats["amazonas"]["especies"].update({"anaconda"})
print(habitats)

