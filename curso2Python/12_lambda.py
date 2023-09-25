# creamos una funcion que incremente un valor:
def increment(x):
    return x + 1
result = increment(10)
print(result)

#transformamos esta funcion en una lambda:
increment2 = lambda x : x + 1
result2 = increment2(20)
print(result2)

#creemos otra lambda recibiendo 2 valores, // .title() es para que cada una de las palabras inicie en mayuscula:
fullName = lambda name, lastName : f"Full name is {name.title()} {lastName.title()}"
text = fullName("calos", "hernández lópez")
print(text)