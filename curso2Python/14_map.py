#creamos una lista y por medio de un for creamos una segunda lista que multiplique todos los valores multiplicados * 2

numbers = [1, 2, 3, 4]
numbers2 = []
for i in numbers:
    numbers2.append(i+2)

print(numbers) #[1, 2, 3, 4]
print(numbers2) #[3, 4, 5, 6]

#los map siempre tienen que estar transformados como una lista.
numbers3 = list(map(lambda i : i * 2, numbers))
print(numbers3) # [2, 4, 6, 8]

#sumamos los elementos de dos listas con lambda, la sumatoria se hace hasta los elemetos de la lista mas pequeña:
numbersA = [1, 2, 3, 4]
numbersB = [5, 6, 7]
print(numbersA) #[1, 2, 3, 4]
print(numbersB) #[5, 6, 7]

result = list(map(lambda x, y: x + y, numbersA, numbersB))
print(result) #[6, 8, 10]

#Ejercicio:

def multiply_numbers(numbers):
    # Escribe tu solución 👇
    numbers2 = list(map(lambda i : i * 2, numbers))
    return numbers2

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)