# and
print("AND")

print("True and True = ", True and True)
print("True and False = ", True and False)
print("False and False = ", False and False)
print("False and True = ", False and True)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

print("*" * 30)
print("Ejemplo AND con Input")

stock = int(input("ingrese el numero de Stock => "))
print(stock >= 100 and stock <= 1000)
print("*" * 30)

# or
print("OR")
print("True or True = ", True or True)
print("True or False = ", True or False)
print("False or False = ", False or False)
print("False or True = ", False or True)

print("*" * 30)
print("Ejemplo OR con Input")

role = input("ingrese el Role => ")
print(role == "admin" or role == "seller") 
print("*" * 30)