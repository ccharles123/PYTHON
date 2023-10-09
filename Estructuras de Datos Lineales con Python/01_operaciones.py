fruits = []

#agregamos elemento a la lista con .append
fruits.append("Melon")
fruits.append("Kiwi")
fruits.append("Berry")

print(fruits) #['Melon', 'Kiwi', 'Berry']

#ordenar de forma alfabetica:
fruits.sort()
print(fruits)#['Berry', 'Kiwi', 'Melon']

#eliminar mi ultimo elemento con .pop(), o eliminar en la posicion que iindico:
fruits.pop()
print(fruits)#['Berry', 'Kiwi']
fruits.pop(1)#['Berry']
print(fruits)#['Berry']

#agregar un elemento en la posicion que quiero con .insert()
fruits.insert(0, "Apple")
print(fruits)#['Apple', 'Berry']
fruits.insert(1,"Straberry")
print(fruits)#['Apple', 'Straberry', 'Berry']

#remover un elemento especifico por su valor, arroja error si el elemento no está en la lista:
fruits.remove("Apple")
print(fruits) #['Straberry', 'Berry']