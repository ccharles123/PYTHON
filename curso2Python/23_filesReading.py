#llamamos al archivo .txt que queremos leer:
#el metodo open es bastante pesado debido a que tiene que leer todo el archivo, se aconseja utilizar el readline() para poder controlar
#la lectura linea a linea
file = open("./text.txt")

#leemos el archivo en su totalidad:
#print(file.read())

#podemos leer linea a linea:
#print(file.readline()) #line 1
#print(file.readline()) #line 2
#print(file.readline()) #line 3

#sin enbargo no sabemos a donde parar porque no sabemos cuantas lineas tiene el archivo, 
# entonces le vamos a decir que vamos aiterar sore las lineas del archivo:
for line in file:
    print(line)
file.close()
#importante saber cuando vamos a cerrar el archivo, esto libera memoria de python

#instruccion que dice que lo abra y que automaticamente lo va ha cerrar es:
with open("./text.txt") as file:
    for line in file:
        print(line)
#es esxactamente igual al anterior pero sin incluir la formula de cerrado.