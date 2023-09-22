person = {
    "name": "Mariana",
    "lastName": "Hernandez",
    "langs": ["Python", "JavaScript"],
    "age": 99
}

print(person)

#Actualizacion de objetos:
person["name"] = "Betty"
print(person)

#Puedo hacer ajustes de los objetos
person["age"] -= 50
print(person)

#puedo agregar en el array otro elmento:
person["langs"].append("C++")
print(person)

#puedo eliminar un atributo en el dict:
del person["lastName"]
print(person)

#otra forma de eliminar atributos es con .pop()
person.pop("age")

#obtener los items de un  dict:
print("Items de person")
print(person.items())

#obtener las keys ó atributos de un  dict:
print("Keys de person")
print(person.keys())

#obtener las values de un  dict:
print("values de person")
print(person.values())

#Ejercicio:
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇

person["twitter"] = "@nicobytes"
person["name"] = "Felipe"
person.pop("age")
print(list(person.keys()))
print(list(person.values()))