entrada = input("Operación: ")
partes = entrada.split(',')

if len(partes) == 3:
    num1_cad = partes[0].strip()
    num2_cad = partes[1].strip()
    operacion = partes[2].strip()

    if num1_cad.replace('.', '', 1).isdigit() and num2_cad.replace('.', '', 1).isdigit():
        num1 = float(num1_cad)
        num2 = float(num2_cad)

        print("-------------")

        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("División por cero.")
        else:
            print("Operación no válida.")
    else:
        print("Números inválidos.")
else:
    print("Formato incorrecto (numero1, numero2, operación)")
