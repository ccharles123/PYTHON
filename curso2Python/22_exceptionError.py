#vamos a manejar este error para que continue las demas lineas de codigo:
try:
    print(0/0)
except ZeroDivisionError as error:
    print("Error")

try:
    assert 1 != 1, "Uno no es igual que Uno"
except AssertionError as error:
    print(error)

#se ejecuta el error y continua con las siguiente lineas:
try:
    age = 10
    if age < 18:
        raise Exception("No se permite menores de edad")
except Exception as error:
    print(error)
print("hola")

#podemos unir todos los try, pero solo va ha verificar el primer error y luego lo detiene:
try:
    print(0/0)
    assert 1 != 1, "Uno no es igual que Uno2"
    age = 10
    if age < 18:
        raise Exception("No se permite menores de edad2")
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
print("hola2")

#ejercicio:

def my_divide(a, b):
    # Escribe tu solución 👇
    try:
        result = a / b
    except ZeroDivisionError as error:
        result = "No se puede dividir por 0"
    return result

    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0


