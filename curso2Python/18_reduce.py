#Reduce una lista a un solo valor:

#tenemos que importar la herramiento reduce:
import functools
#creamos una lista:

numbers = [1, 2, 3, 4]

#reducimos a un solo numero que es la sumatoria de todos los valores:  
result = functools.reduce(lambda counter, item: counter  + item, numbers)
print(result)#10

#miremos el anterior proceso en una funcion:
def accum(counter, item):
    print ("counter =>",counter)
    print ("Item =>",item)
    return counter + item

result2 = functools.reduce(accum, numbers)
print("Resultado final =>",result2)

