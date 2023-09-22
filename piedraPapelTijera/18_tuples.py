#TUPLES

numbers = (1, 2, 3, 5)
strings = ("Mariana", "Betty", "Bombon", "Mariana")

print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

# Puedo consultar las posiciones de la Duple, inicio final, etc.
print("0 => ", numbers[0])
print("-1 => ", numbers[-1])

# La DUPLE es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data 
# si no queremos que se modifique por error, solo con se lectura.

#Metodos de la DUPLE:

#VER cual es la primera POSICION donde está NUESTRO ELEMENTO:

print(strings)
print("posicion de Mariana => ", strings.index("Mariana"))

# VER QUE CUANTAS VECES ESTÁ NUESTRO ELEMENTO:

print("cuantas veces está de Mariana => ", strings.count("Mariana"))

# podemos hacer transformaciones, puedo cambia de DUPLE  a LIST

myList = list(strings)
print(myList)

# Siendo list puedo modificar
myList[0] = "Edimer"
print(myList)

# podemos hacer transformaciones, puedo cambia de LIST a DUPLE
myDuple = tuple(myList)
print(myDuple)


