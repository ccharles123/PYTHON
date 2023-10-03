#llamamos nuestro modulo y lo ejecutamos en el main:
import utils2
import readCSV2
import graficas2
import pandas as pd

def run():
    
    while True:
        data = readCSV2.readCsv("./data2.csv")
        country = input("Type Country => ")
        
        result = utils2.populationsByCountry(data, country)
        
        if len(result) > 0: 
            countryDictionary = result[0]
            labels, values = utils2.getPopulations(countryDictionary)
            graficas2.generateBarChart(country, labels, values)
            print(f"Se generó imagen de la grafica de la poblacion el country: {country}, en la carpeta imgs/country")
            break
        else: 
            print("EL country ingresado no es valido, favor ingresar el country nuevamente: ")

    while True:
        continent = input("Ingresar el continente que deseas graficar su población => ")
        #data = readCSV2.readCsv("./data2.csv")#informacion del csv en formato dictionary
        #data = list(filter(lambda x : x["Continent"] == continent, data))#podemos filtrar por continente
        
        if len(data) > 0:
            #columnCountries = list(map(lambda x : x["Country"], data)) #sacamos la columna de cada uno de los paises de la data2 con map
            #columnPorcentages = list(map(lambda x : x["World Population Percentage"], data))#sacamos el porcentaje de la columna de porcentajes de la data2
            
            #utilizamos libreria -----PANDAS----- para leer nuestro data2.csv:
            df = pd.read_csv("data2.csv")
            df = df[df["Continent"] == continent]
            
            #optener la columnas paises y columna porcentajes:
            columnCountries = df["Country"].values
            columnPorcentages = df["World Population Percentage"].values
            
            graficas2.generatePieChart(continent, columnCountries, columnPorcentages)
            print(f"Se generó imagen de la grafica de la poblacion del continent: {continent}, en la carpeta imgs/continent")
            break
        else:
            print("Continente no encontrado. Por favor, ingrese un continente válido.")
            
#con el siguiente if podemos ejecutar el archivo desde otro module o desde la terminal llamando al main:
if __name__ == '__main__':
    run()