import matplotlib.pyplot as pyplot

def generatePieCharts():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]
    
    fig, ax = pyplot.subplots()
    ax.pie(values, labels=labels)
    pyplot.savefig("pie.png") #guarda la grafica como pie.png en nuestro proyecto.
    pyplot.close