#creamos este modulo con la siguiente funcion:

def getPopulations(countryDictionary):
    populationDict = {
        "2022" : int(countryDictionary["2022 Population"]),
        "2020" : int(countryDictionary["2020 Population"]),
        "2015" : int(countryDictionary["2015 Population"]),
        "2010" : int(countryDictionary["2010 Population"]),
        "2000" : int(countryDictionary["2000 Population"]),
        "1990" : int(countryDictionary["1990 Population"]),
        "1980" : int(countryDictionary["1980 Population"]),
        "1970" : int(countryDictionary["1970 Population"])
    }
    labels = populationDict.keys()
    values = populationDict.values()
    return labels, values

#creamos una funcion obtener una poblacion basada de un pais:

def populationsByCountry(data, country):
    result = list(filter(lambda item: item["Country"] == country, data))
    return result



