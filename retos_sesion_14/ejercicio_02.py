def calcular(num1, num2, ope):
    if ope == '+':
        return num1 + num2
    elif ope == '-':
        return num1 - num2
    elif ope == '*':
        return num1 * num2
    elif ope == '/':
        if num2 == 0:
            return "Error: división por cero"
        return num1 / num2
    else:
        return "Operación no válida"

op1 = calcular(10, 5, "+")
print(op1)
