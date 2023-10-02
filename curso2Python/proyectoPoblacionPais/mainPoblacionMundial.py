#llamamos nuestro modulo y lo ejecutamos en el main:
import readCSV2
import graficas2
#vamos a graficar solo la columna de porcentajes de los paises:
def run():
    while True:
        continent = input("Ingresar el continente que deseas graficar su población => ")
        data = readCSV2.readCsv("./proyectoPoblacionPais/data2.csv")#informacion del csv en formato dictionary
        data = list(filter(lambda x : x["Continent"] == continent, data))#podemos filtrar por continente
        if len(data) > 0:
            columnCountries = list(map(lambda x : x["Country"], data)) #sacamos la columna de cada uno de los paises de la data2 con map
            columnPorcentages = list(map(lambda x : x["World Population Percentage"], data))#sacamos el porcentaje de la columna de porcentajes de la data2
            graficas2.generatePieChart(columnCountries, columnPorcentages)
            break
        else:
            print("Continente no encontrado. Por favor, ingrese un continente válido.")
        
        
    


#con el siguiente if podemos ejecutar el archivo desde otro module o desde la terminal llamando al main:
if __name__ == '__main__':
    run()