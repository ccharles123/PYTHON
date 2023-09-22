if True:
    print("deberia ejecutarse")

if False:
    print("nunca se ejecuta")
    
# Ejemplo con Mascotas con elif

pet = input("¿Cual es tu mascota favorita? => ")
if pet == "perro":
    print("Genial tienes buen gusto")
elif pet == "gato":
    print("Espero tengas suerte")
elif pet == "pez":
    print("Eres lo maximo")
else:
    print("No tienes ninguna mascota interesante")

# Ejemplo con If y Else con un stock de inventario:
'''
stock = int(input("Ingrese el numero de Stock => "))

if stock >= 100 and stock <= 1000:
    print("El stock es correcto ")
else:
    print("El stock es incorrecto ")
'''

#Ejercicio un numero es par o impar

numero = int(input("ingresa un numero => "))

if numero % 2 == 0:
    print("El numero es PAR")
else:
    print("El numero es IMPAR")

