#filtra elemento de una lista:
numbers = [1, 2, 3, 4, 5]

#filtramos los numero pares:
filterParNumbers = list(filter(lambda i: i % 2 == 0, numbers)) 
print(filterParNumbers)

#filtramos los impares:
filterImparNumbers = list(filter(lambda i: not i % 2 == 0, numbers)) 
print(filterImparNumbers)

#no se ha midificado la lista original:
print(numbers)

#ejercicio: 

def filter_by_length(words):
# Escribe tu solución 👇
    wordsLenMayor4 = list(filter(lambda items : len(items) >= 4, words))
    return wordsLenMayor4 

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)