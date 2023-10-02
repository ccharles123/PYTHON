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