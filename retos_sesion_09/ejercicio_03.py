nombres = [
    "Eric",
    "Stan",
    "Kyle",
    "Kenny",
    "Butters",
    "Randy",
    "José",
    "Wendy",
    "Towelie",
    "Heidi"
]
sub_lista = nombres[5:9:2]
print("Sublista:", sub_lista)

existe_jose = "José" in nombres
print("¿Existe José? ->", existe_jose)

sub_lista.sort()
print("Sublista ordenada (A-Z):", sub_lista)

nombres.sort(reverse=True)
print("Lista original ordenada (Z-A):", nombres)
