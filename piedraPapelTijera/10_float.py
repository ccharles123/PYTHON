x = 3.3
print(x)#3.3
y = 1.1 + 2.2
print(y)#3.30000003

print(x == y)#false porque no son precisos

#comparacion de string
yString = format(y, ".2g")# lo convertimos en string y le pido que solo me imprima 2 digitos
print("Es un string " + yString)

print(yString == str(x))

print("*" * 20)#linea divisoria

#comparacion forma matematica

print(x, y)
tolerancia = 0.00001

print(abs(x - y) < tolerancia) #abs es el valor absoluto de la operacion
