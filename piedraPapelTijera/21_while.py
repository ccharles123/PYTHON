'''
while True:
    print("Se ejecutó")
'''
#el ciclo while se detiene siempre y cuando se cumpla una condicion:
'''
counter = 0
while counter < 10:
    counter += 1
    print(counter)
'''

#podemos romper el ciclo con un break
'''
counter = 0
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''

#funcion continue, continua un conteo si cumple con una condicion, ejemplo:
counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter) 