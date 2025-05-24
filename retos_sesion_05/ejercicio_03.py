# Total de segundos
total_segundos = 1000000

# Conversión
semanas = total_segundos // (7 * 24 * 60 * 60)
resto = total_segundos % (7 * 24 * 60 * 60)

días = resto // (24 * 60 * 60)
resto = resto % (24 * 60 * 60)

horas = resto // (60 * 60)
resto = resto % (60 * 60)

minutos = resto // 60
segundos = resto % 60

print(total_segundos, "segundos =", semanas, "semanas", días, "días", horas, "horas", minutos, "minutos", segundos, "segundos")
