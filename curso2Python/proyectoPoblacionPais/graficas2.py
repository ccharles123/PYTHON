#importo libreria para graficar y le coloco el alias plt
import matplotlib.pyplot as plt

#hago una funcion:
def generateBarChart(labels, values):
    fig, ax =plt.subplots()
    ax.bar(labels, values)
    plt.show()

#generemos un grafico de torta:
def generatePieChart(labels, values):
    fig, ax =plt.subplots()
    ax.pie(values,labels = labels)
    ax.axis("equal")
    plt.show()
    
#para ejecuatar con un script en nuestro terminal y se envian los valores a la funcion generateBarChart:
if __name__ == "__main__":
    labels = ["Mariana", "Edimer", "Carlos"]
    values = [10, 33, 38]
    #generateBarChart(labels, values)
    generatePieChart(labels, values)
