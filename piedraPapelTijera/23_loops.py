#hacemos una tabla con 3 listas internas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#así visualizo una fila ó la primera lista:
print(matriz[0])

#así visualizo una posición especifica:
print(matriz[0][1])

#hacemos una iterarción con for, 
# vamos a visulizar cada una de las listas ó filas de manera individual:
for row in matriz:
    print(row)

#vamos a visulizar cada una de los elemento de manera individual:
for row in matriz:
    for column in row:
        print(column)

