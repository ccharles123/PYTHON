#importo libreria para graficar y le coloco el alias plt
import matplotlib.pyplot as plt

#hago una funcion:
def generateBarChart(country, labels, values):
    fig, ax =plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"./imgs/country/{country}.png") #guarda la grafica con el nombre del pais en png en nuestro proyecto y lo guarda en carpeta.
    plt.close

#generemos un grafico de torta:
def generatePieChart(continent, labels, values):
    fig, ax =plt.subplots()
    ax.pie(values,labels = labels)
    ax.axis("equal")
    plt.savefig(f"./imgs/continent/{continent}.png") #guarda la grafica como pie.png en nuestro proyecto.
    plt.close
    
#para ejecuatar con un script en nuestro terminal y se envian los valores a la funcion generateBarChart:
if __name__ == "__main__":
    labels = ["Mariana", "Edimer", "Carlos"]
    values = [10, 33, 38]
    #generateBarChart(labels, values)
    generatePieChart(labels, values)
