text = "Ella sabe Python"

# Puedo ingresar a nivel de posiciones la ubicacion de una cadena de String

print(text[0])
print(text[1])

# ir a la ultima posicion

size = len(text)
print("size => ", size)
print(text[size - 1])
print(text[-1])

# slicing: muestra una cadena de texto iniciando en una posición a otra no incluye los extremos:

print(text[0:4])
print(text[5:9])
print(text[10:16])
print(text[:9])
print(text[5:-1])#no invluye el final
print(text[5:])#incluye el final
print(text[:]) #desde inicio hasta final
print(text[10:16:1])#toma la cadena de la posicion 10 hasta la 16 y va de 1 salto de la posicion
print(text[10:16:2])#toma la cadena de la posicion 10 hasta la 16 y va de 2 salto de la posicion
print(text[::2])#toma la cadena del inicio hasta el final y va de 2 salto de la posicion

