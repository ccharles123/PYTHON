#Conjuntos, en un conjunto no podemos tener elementos repetidos:

setCountries = {"colombia", 'mexico', 'argentina', "colombia"}
print(setCountries)
print(type(setCountries)) #automaticamente elimina elementos repetidos

# se puede crear conjuntos de numeros
setNumbers = {2, 4, 6, 443, 2}
print(setNumbers)
print(type(setNumbers)) #automaticamente elimina elementos repetidos

# se puede crear conjuntos de diferentes tipos
setTypes = {2, "hola", False, 12.12}
print(setTypes)
print(type(setTypes)) #automaticamente elimina elementos repetidos

#crear un conjunto a partir de un string
setFromString = set("hola")
print(setFromString)

#crear un conjunto a partir de una duple
setFromDuples = set(("abc", "def", "ghi", "abc"))
print(setFromDuples)

#crear un conjunto a partir de una list
numbers = [1, 2, 3, 1, 2, 3, 4]
setFromNumbers = set(numbers)
print(setFromNumbers) #automaticamente elimina elementos repetidos
listNumbersFilters = list(setFromNumbers) #luego de filrado los numeros puedo pasarlos a formato lista 
print(listNumbersFilters)