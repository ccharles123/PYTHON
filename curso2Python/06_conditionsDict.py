#creamos un dictionary simulando la poblacion (aleatoria) de cada country de countries

import random
countries = ["colombia", "mexico", "bolivia"]

populations2 = {country: random.randint(1, 100) for country in countries}
print(populations2)

#agregamos una condicional de que solo me muestre los paises con poblacion mayor a 50

result = {country: population for (country, population) in populations2.items() if population > 50}
print(result)

#generemos un dictionary con las vocales de un string sin repetirse:

text= "hola soy Mariana Hernandez"
dictVocals = { c: c.upper() for c in text if c in "aeiou"}
print(dictVocals)

dictVocals2 = { c: c.count(c) for c in text}
print(dictVocals2)
