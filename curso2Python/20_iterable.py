#imprimimos los numero del 1 al 10 

for i in range(1, 11):
    print(i)

myIter = iter(range(1, 4))
print(myIter)

#con el siguiente metodo next(), puedo iterar de forma manual, así:
print(next(myIter))#1
print(next(myIter))#2
print(next(myIter))#3
print(next(myIter))#arroja error debido a que el 4 es el limite