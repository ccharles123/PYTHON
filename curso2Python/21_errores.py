#print(0/0)
#cuando imprimimos una variable que no está declarada sale un error y este hace que python no corra el resto del codigo:
#print(result)
print("Hola")

suma = lambda x, y : x + y

#con el siguiente codigo puedes verificar si el codigo está tal cual como deberia:
assert suma(2, 2) == 4

print("Hola 2")

#en el siguiente codigo puedo lanzar mi propia exceptio de error, no se van ha ejecutar las lineas despues de esta:
age = 10
if age < 18:
    raise Exception("No se permite menores de edad")