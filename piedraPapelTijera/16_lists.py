numbers = [1, 2, 3, 4]

print(numbers)
print(type(numbers))

#creamos una lista de tareas:

tasks = ["make a dishes", "play video games"]
print(tasks)

types = [1, True, "hola"]
print(types)
print(numbers[0])
print(tasks[0])

# Puedo reemplazar la posicion que quiera en el array, en este caso reemplazo la posicion 0 del array types 
types[0] = 10
print(types)

tasks[0] = "watch platzi courses"
print(tasks)

tasks[0] = "do the dishes"
print(tasks)

# En los arrays puedo seleccionar un grupo de posociones así:

print(numbers[:3])

#piedo utilizar el IN para saber si hay un caracter en la lista este devuelve un boolean:

print(True in types)
print("ola" in types)
