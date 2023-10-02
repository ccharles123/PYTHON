import readCSV
import graficos

def count_and_plot_types_by_country(country):
    type_counts = {}

    data = readCSV.readNetflixCsv("./netflixTitles.csv")

    for entry in data:
        if entry["country"] == country:
            type = entry["type"]
            if type in type_counts:
                type_counts[type] += 1
            else:
                type_counts[type] = 1

    if not type_counts:
        print(f"No se encontraron datos para el país '{country}'.")
        return

    labels = list(type_counts.keys())
    values = list(type_counts.values())

    graficos.generateBarChart(labels, values)
    graficos.generatePieChart(labels, values)

if __name__ == "__main__":
    country = input("Por favor, ingresa el país para contar y graficar los tipos de contenido: ")
    count_and_plot_types_by_country(country)




