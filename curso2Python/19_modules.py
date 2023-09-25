#miremos un modilo para preguntar el sistema operativo donde estamos ejecutando el programa
import sys
print(sys.path)

#tiene que ver con expresiones regulares (nos invitan a tomar el curso de expreciones regulares):
import re
text = "mi numero de telefono es:  3013095701, el codigo del pais es 57, mi numero de la suerte es 3 "

#con una exprecion regular podemos ver solo los numeros que conicidan en este texto:
result = re.findall("[0-9]+", text)
print(result)

#manejo de horas y fechas:
import time

#imorimir fecha y hora actual con timestamp
timetamp = time.time()
print(timetamp)#nos arroja la fecha y hora formato pc

local = time.localtime()
result = time.asctime(local)#nos arroja la fecha y hora formato lectura
print(result)

#colections, utlidad para llamar listas:
import collections
numbers = [1, 2, 1, 1, 2, 2, 4, 3, 5, 3, 4, 3]

#vamos a ver cual es la frecuencia de un numero en esta lista:
counter = collections.Counter(numbers)
print(counter)