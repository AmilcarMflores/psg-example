serie = []

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        serie.append("FizzBuzz")
    elif i % 5 == 0:
        serie.append("Fizz")
    elif i % 7 == 0:
        serie.append("Buzz")
    else:
        serie.append(i)

for numero in serie:
    print(numero)
