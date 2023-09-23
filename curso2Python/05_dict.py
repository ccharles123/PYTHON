#crear una dict con un rango iterable de 10 elementos:
numbers = {}
for i in range(1, 5):
    numbers[i] = i * 2
print(numbers)

# creamos con la sintaxi de la dict:
numbers2 = {i: i * 2 for i in range(1, 5)}
print(numbers2)

# generar el dict a partir de una lista forma clasica que me agregue un numero aleatorio de 1  a 100:
import random
countries = ["colombia", "mexico", "bolivia"]
populations = {}

for country in countries:
    populations[country] = random.randint(1, 100)
print(populations)

# otra forma de hacerlo con la syntaxis:
populations2 = {country: random.randint(1, 100) for country in populations}
print(populations2)

# generar el dict a partir de dos listas:
names = ["Mariana", "Betty", "Edimer"]
age = [10, 50, 33]
print(list(zip(names, age)))
dictUsuarios = {name: age for (name, age) in zip(names, age)}
print(dictUsuarios)


