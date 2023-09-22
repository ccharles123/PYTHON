# CRUD Create, Read, Update and Delete

# Read
numbers = [1, 2, 3, 4, 5]
print(numbers[0])

# Update
numbers[-1] = 10
print(numbers)

# Create un elemento al final de la lista .append()
numbers.append(700)
print(numbers)

#agregar en cualquier posicion de la lista con .insert(posicion, valor a insertar)
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "change")
print(numbers)

# Fusionar lista
tasks = ["todo1", "todo2", "todo3"]
newList = numbers + tasks
print(newList)

# Preguntar en que posicion está un elemento en una lista .index(valor a buscar):
index = newList.index("todo2")
print(index)
newList[index] = "todo changed"
print(newList)

# Delete eliminar elemntos de una lista .remove(valor a elimiar)
newList.remove("todo1")
print(newList)

# elimina el ultimo elemento de esta lista .pop() ó la posicion que tu desees .pop(posicion a eliminar)
newList.pop()
print(newList)

newList.pop(0)
print(newList)

#Cambiar de manera reversa la posicion del array .reverse()
newList.reverse()
print(newList)

#ordenar una lista de menor a mayor .sort() aplica para numeros y strings
numbers1 = [3, 6, 1, 8, 2, 7, 8]
numbers1.sort()
print(numbers1)

strings = ["ab", "bc", "aa", "bb", "ca"]
strings.sort()
print(strings)

# No funciona para ordenar arrays con types mezclados, devueve error
#newList.sort()
#print(newList)

#limpiar una lista
newList.clear()
print(newList)


# Delete
#numbers.delete()
#print(numbers)