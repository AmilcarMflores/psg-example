def calculadora():
    while True:
        try:
            num1 = input("Ingrese el primer número (o 'salir' para terminar): ")
            if num1.lower() == "salir":
                print("Calculadora finalizada")
                break
            num2 = input("Ingrese el segundo número: ")
            if num2.lower() == "salir":
                print("Calculadora finalizada")
                break

            num1 = float(num1)
            num2 = float(num2)

        except ValueError:
            print("Error: Debe ingresar un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        else:
            print(f"Suma: {num1 + num2}")
            print(f"Resta: {num1 - num2}")
            print(f"Multiplicación: {num1 * num2}")
            try:
                print(f"División: {num1 / num2}")
            except ZeroDivisionError:
                print("Error: No se puede dividir entre cero.")
        finally:
            print("Operación completada\n")

calculadora()
