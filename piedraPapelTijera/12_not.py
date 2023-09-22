print(not True)
print(not False)

# NOT AND
print("NOT AND")

print("not True and True = ", not(True and True))
print("not True and False = ", not(True and False))
print("not False and False = ", not (False and False))
print("not False and True = ", not(False and True))

print("*" * 30)
print("Ejemplo not AND con Input")

stock = int(input("Ingrese el numero de Stock => "))
print(not(stock >= 100 and stock <= 1000))
print("*" * 30)