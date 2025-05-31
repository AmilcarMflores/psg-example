print("Operador XNOR")
a = True
b = False
print(not ((a or b) and not (a and b)))  # False

a = True
b = True
print(not ((a or b) and not (a and b)))  # True

a = False
b = False
print(not ((a or b) and not (a and b)))  # True

a = False
b = True
print(not ((a or b) and not (a and b)))  # False
