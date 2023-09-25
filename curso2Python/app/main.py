#llamamos nuestro modulo y lo ejecutamos en el main:
import utils

data = [
    {
        "Country": "Colombia",
        "Populations": 200,
    },
    {
        "Country": "Bolivia",
        "Populations": 300,
    },
    {
        "Country": "Brasil",
        "Populations": 500,
    }
]

def run():
    keys, values = utils.getPopulations()
    print(keys, values)

    #podemos imprimir variables del modulo mod:
    print(utils.text)

    #enviamos la información para que nos filtre por ciudad la poblacion:

    country = input(f"favor ingresar el pais para consultar su población => ")

    result = utils.populationsByCountry(data, country)
    print(result)


#con el siguiente if podemos ejecutar el archivo desde otro module o desde la terminal llamando al main:
if __name__ == '__main__':
    run()