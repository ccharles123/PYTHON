# FOR: imprimir numero del 0 al 19:
'''
for element in range(20):
    print(element)
'''
#imprimir numero del 1 al 20:
'''
for element in range(1, 21):
    print(element)
'''

#recorremos una list, tuple y dict:
myList = [23, 45, 67, 89, 43]
for element in myList:
    print(element)

tuple = ("Mariana", "Betty", "Edimer")
for element in tuple:
    print(element)

product = {
    "name": "Camisa",
    "price": 100,
    "stock": 89    
}

#iteracion de solo las keys o atributos de un dict:
for keys in product:
    print(keys)

#iteracion de los valores de las keys o atributos de un dict:
for keys in product:
    print(keys, "=>", product[keys])

#otra forma de ver los valores de las keys de un dict:
for key, value in product.items():
    print(key, "=>", value) 

#Se puede encontrar en la programacion listas con dict adentro ejemplo:
listPerson = [
    {
        "name": "Mariana",
        "age": 10
    },
    {
        "name": "Betty",
        "age": 40
    },
    {
        "name": "Edimer",
        "age": 33
    }
]

#iterar esta lista de personas que contienen keys en su dict:
for person in listPerson:
    print("name", "=>", person["name"])
    print("age", "=>", person["age"])
    
#ejercicio:

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for positivos in my_list:
    if positivos > 0:
        new_list.append(positivos)
print(new_list)
