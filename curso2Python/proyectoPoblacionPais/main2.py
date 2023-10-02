#llamamos nuestro modulo y lo ejecutamos en el main:
import utils2
import readCSV2
import graficas2

def run():
    
    while True:
        data = readCSV2.readCsv("./proyectoPoblacionPais/data2.csv")
        country = input("Type Country => ")
        
        result = utils2.populationsByCountry(data, country)
        print(result)
        
        if len(result) > 0: 
            countryDictionary = result[0]
            print(countryDictionary)
            labels, values = utils2.getPopulations(countryDictionary)
            graficas2.generateBarChart(labels, values)
            break
        else: 
            print("EL country ingresado no es valido, favor ingresar el country nuevamente: ")


#con el siguiente if podemos ejecutar el archivo desde otro module o desde la terminal llamando al main:
if __name__ == '__main__':
    run()