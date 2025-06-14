notas_semestre = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
print(type(notas_semestre))

promedio_final = sum(notas_semestre) / len(notas_semestre) >= 51
print(f'¿Aprobó el estudiante? -> Resp.: {promedio_final}')