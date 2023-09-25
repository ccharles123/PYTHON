#creamos este modulo con la siguiente funcion:

def getPopulations():
    keys = ["col", "bol"]
    values = [300, 400]
    return keys, values

#creamos variables:
text = "Hola"

#creamos una funcion obtener una poblacion basada de un pais:

def populationsByCountry(data, country):
    result = list(filter(lambda item: item["Country"] == country, data))
    return result

