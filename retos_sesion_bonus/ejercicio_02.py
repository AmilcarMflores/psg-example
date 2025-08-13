import random

def obtener_aleatorio():
    return random.randint(1, 100)

def adivina(secreto):
        intentos = 0
        print ("Que número estoy pensando? (1-100)")
        while True:
            entrada = input(f"Intento N°: {intentos+1}: ").strip()
            try:
                intento = int(entrada)
            except ValueError:
                print("Por favor, ingresa un número válido o escribe 'salir' para terminar.")
                continue
            
            if not 1 <= intento <= 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            intentos += 1

            if intento == secreto:
                print ("Felicidades! Has adivinado el número!")
                break
            elif intento < secreto:
                print ("El número es mayor.")
            else:
                print ("El número es menor.")
        print (f"Has adivinado el número en {intentos} intentos.\n")
        return True

def jugar():
        print ("Bienvenido al juego de adivinanzas! del Python Study Group 2025")
        print ("="*63)
        nombre_jugador = input("¿Cuál es tu nombre?: ").strip() or "Guest"
        print (f"Bienvenido, {nombre_jugador}!")
        print ("="*63)
        print ()

        while True:
            opcion = input("Quieres jugar? (s/n): ").strip().lower()
            if opcion != 's':
                break
            secreto = obtener_aleatorio()
            adivina(secreto)

        print ("Gracias por participar!")
        print (f"🐍 Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()