# Primera funcion es print:
print("hola")

# Segunda funcion:
def myPrint(text):
    print("This is my print")
    print(text * 2)
myPrint("Este es mi texto")
myPrint("Este es mi segunto texto")

# Hacemos una funcion para sumar 2 vaores enviados por parametros:
def suma (a, b):
    c = a + b
    print(c)
    myPrint(c) #utilizamos la funcion myPrint dentro de la funcion suma
suma(2, 4)
suma(10, 15)



