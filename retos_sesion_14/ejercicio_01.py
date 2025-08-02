def promedio(lista_calificaciones):
    total = sum(lista_calificaciones)
    return total / len(lista_calificaciones)

calificaciones = [50, 75, 80, 91, 70]
respuesta = promedio(calificaciones)
print(f'El promedio de las calificaciones: {calificaciones} es: {respuesta}')