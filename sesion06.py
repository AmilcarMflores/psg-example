print("Tipos de datos booleanos")
print(True)
print(False)

# Operaciones aritméticas con booleanos
print (True + True) #2
print (True * True) #1
print (True * False) #0
print (False + False) #0
print (False * False) #0

# Números y booleanos
print (10 + True) #11
print (10 + False) #10
print (10 * True) #10
print (10 * False) #0

# Declarar variables booleanas
var_booleana = True
print(type(var_booleana)) #<class 'bool'>
var_booleana = False
print(type(var_booleana)) #<class 'bool'>

# Otra forma de declarar
var_booleana = bool(1)
print(var_booleana) #True
print(type(var_booleana)) #<class 'bool'>
var_booleana = bool(0)
print(var_booleana) #False
var_booleana = bool(-15) # Solo el 0 pueder ser falso, lo demás te dará True
print(var_booleana) #True


# Operadores de comparación (<, >, <=, >=)

# Operadores de igualdad e identidad (==, !=, is, is not)
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
print (10 is 10)
print (10 is not 10)


# Asignación de variables
x = 10
mayor_que_cero = x > 0
print(mayor_que_cero)
diferente_de_10 = x != 10
print(diferente_de_10)

# Operadores lógicos (not, and, or)
# Tienen un orden en la ejecución: primero se ejecuta el not, and y or)
print("gato" or "gato")
print("gato" or "perro")


# Ejercicio 1 - Determinar si el número 20 está en el rango 0 a 100

numero = 20

rango_inferior = numero >= 0
rango_superior = numero <= 100

resultado = rango_inferior and rango_superior
print(resultado)

# Si es True está en este rango
# Si es False no está en este rango

# Ejercicio 2
primer_puntaje = 15
segundo_puntaje = 20
tercer_puntaje = 16

suma_total_puntaje = primer_puntaje + segundo_puntaje + tercer_puntaje

print(suma_total_puntaje > 50) # Aprobo si es True

# Ejercicio 3
numero = 15
es_divisible = ((numero % 3 == 0) and (numero % 5 == 0)) and not (numero % 2 == 0)
print("El número", numero, "¿es divisible por 3 y 5 pero no por 2?:", es_divisible) 


# Cortocircuito con operador and
x = 3 + 5
y = 0

#print(x < 2 and ( x / y) > 2)
#print(x > 0 and (x / y) > 0)

# Cortocircuito con operador or
x = 1
y = 0

#print(x > 0 or (x / y) > 0)
#print(x > 2 or (x / y) > 2)

