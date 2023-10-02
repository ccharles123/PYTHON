#importamos la funcion csv, vamos a leer un csv y transformamos a ditionario:
import csv

#creamos una funcion para leer el archivo:
def readCsv(path):
    with open(path, "r") as csvFile:
        reader = csv.reader(csvFile, delimiter=",") #el delimitador es que lo datos vienen separados por coma.
        header = next(reader) #obtener la primera fina de forma manual, seria los nombres de las columnas.
        #print(header)
        data = []#aqui vamos almacenar el nuevo array con los dictionary
        for row in reader:
            iterable = zip(header, row)#va unir el header y el row como un array de duplas, primera posicion columna y segunda posicion el row.
            #print(iterable)
            countryDictionary = {key: value for key, value in iterable}#los convertimos en distionary con key value.
            #print(countryDictionary)
            data.append(countryDictionary)#insertamos en el array vacio la informacion.
        return data

#lo corremos como un script desde la terminal con un if:
if __name__ == "__main__":
    data = readCsv("./proyectoPoblacionPais/data2.csv")
    print(data[0])#nos muestra un array como un dictionary
