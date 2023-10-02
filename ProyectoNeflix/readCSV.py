#importamos la funcion csv, vamos a leer un csv y transformamos a dictionario:
import csv

#creamos una funcion para leer el archivo:
def readNetflixCsv(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as csvFile:
        reader = csv.reader(csvFile, delimiter=",") #el delimitador es que lo datos vienen separados por coma.
        header = next(reader) #obtener la primera fina de forma manual, seria los nombres de las columnas.
        #print(header)
        data = []#aqui vamos almacenar el nuevo array con los dictionary
        for row in reader:
            row = [item.strip('"') for item in row]
            iterable = zip(header, row)#va unir el header y el row como un array de duplas, primera posicion columna y segunda posicion el row.
            #print(iterable)
            netflixDictionary = {key: value for key, value in iterable}#los convertimos en distionary con key value.
            #print(netflixDictionary)
            data.append(netflixDictionary)#insertamos en el array vacio la informacion.
        return data

#lo corremos como un script desde la terminal con un if:
if __name__ == "__main__":
    data = readNetflixCsv("./netflixTitles.csv")
    print(data[2000])#nos muestra un array como un dictionary