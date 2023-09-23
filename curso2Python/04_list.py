#crear una lista con un rango iterable de 10 elementos:
numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)

# muestra 10 numeros pares ó multiplos de 2:
numbers2 = []
for element in range(1, 11):
    numbers2.append(element * 2)
print(numbers2)

#otra forma de hacerlo una lista con un rango iterable de 10 elementos con sintaxis mas corta y facil de leer es:
numbers2 = [element for element in range(1,11)]
print(numbers2)

#otra forma de hacerlo una lista con un rango iterable de 10 elementos multiplos de 2, es:
numbers3 = []
numbers3 = [element * 2 for element in range(1,11)]
print(numbers3)

# agregamos condiciones al iterable, para que nos muestre lo numero pares entre 1 y 11:
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)

#otra forma de hacerlo con la sintaxis iterable:
numbers2 = [i for i in range(1,11) if i % 2 == 0]
print(numbers2)