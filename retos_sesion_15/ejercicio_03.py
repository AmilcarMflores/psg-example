class FondosInsuficientesError(Exception):
    pass

def cajero():
    saldo_disponible = 5000
    while True:
        try:
            monto = input("Ingrese el monto a retirar (o 'salir' para terminar): ")
            if monto.lower() == "salir":
                print("Operación finalizada")
                break

            monto = float(monto)

            if monto <= 0:
                raise ValueError("El monto debe ser mayor a 0")
            if monto > 1000:
                raise Exception("El monto excede el límite permitido por transacción (1000)")
            if monto > saldo_disponible:
                raise FondosInsuficientesError("No hay fondos suficientes")

        except ValueError as e:
            print(e)
        except FondosInsuficientesError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            saldo_disponible -= monto
            print(f"Retiro exitoso. Saldo restante: {saldo_disponible}")
        finally:
            print("Transacción procesada\n")

cajero()
