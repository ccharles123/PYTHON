# Diccionarios ó Objetos

myDict = {}
print(type(myDict))

myDict = {
    'avion' : 'Boing',
    'name' :  'Mariana',
    'last_name' : 'Hernandez',
    'age' : 10
}
print(myDict)

#podemos saber cuantos elementos hay en este dict
print(len(myDict))

#leer los valores que me interesan en el dict, aquí me arroja el valor del nombre buscado, de no existir arroja un error.
print(myDict["name"])
print(myDict["last_name"])

#otra forma de hacerlo con .get(), la dicferencia es que si no lo consigue arroja un None
print(myDict.get("hola"))

#podemos validar si hay un elemento en mi dict, arroja un boolean
print("avion" in myDict)
print("otroQueNo" in myDict)
