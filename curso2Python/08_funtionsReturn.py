# Creamos una logica que nos muestre el resultado sea sum = 10! (sumatoria 1+2+3+4+5+6+7+8+9) 

sum = 0
for x in range(1, 10):
    sum += x
print(sum)

#creamos una funcion con esta logica adentro y la hacemos mas dinamicas:

def SumRange(min, max):
    print(f"Para un min => {min} y un max => {max} el resutado es: ")
    sum = 0
    for x in range(min, max):  
        sum += x
    return sum
result1 = SumRange(1, 10)
print(result1)

result2 = SumRange(10, 20)
print(result2)

#podemos utilizar el resultado de la funcion para enviarla por parametro así:
result3 = SumRange(result1, result2 + 10)
print(result3)
