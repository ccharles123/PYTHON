# creamos una funcion con 3 parametros, por defecto le podemos asignar valores en el caso que no sea enviado como parametro,
# tambien la funcion puede retornar varias variables, en este caso retorna el calculo, un string y un parametro:
def findVolume(length=1, width=1, depth=1):
    return length * width * depth, "el length es: ", length

result1 = findVolume(10, 10, 10)
print(result1)

result2 = findVolume()
print(result2)

#puedo enviar solo una variable así:
result3 = findVolume(width=10)
print(result3)

#puedo imprimir el valor de la posicion del uno de los resultados así:
print(result3[0])

#otra forma de imprimir los valores de los resultados es:
result4, text, length = findVolume(width=10)
print(result4)
print(text)
print(length)
