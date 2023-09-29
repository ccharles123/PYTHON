#para poder escribir debo tener permisos de escritura y se le coloca "r+"
with open("./text.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("nuevas cosas en este archivo\n") #para generar un salto de linea debemos colocar al final \n
    file.write("otra linea\n")
    file.write("otra linea mas\n")

#ahora si queremos sobre escribir lo que tiene el archivo por una nuevas lineas "w+", hacemos lo siguiente:

with open("./text.txt", "w+") as file:
    for line in file:
        print(line)
    file.write("nuevas cosas en este archivo\n") #para generar un salto de linea debemos colocar al final \n
    file.write("otra linea\n")
    file.write("otra linea mas\n")