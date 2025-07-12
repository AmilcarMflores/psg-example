pregunta = tuple(input("Ingresa una pregunta: ").split())

tupla_concatenada = ('¿', ) + pregunta + ('?', )
print(tupla_concatenada)
print(type(tupla_concatenada))

tupla_repetida = 2 * tupla_concatenada
print(tupla_repetida)