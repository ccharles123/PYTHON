import requests

def getCategories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)#vemos que estatus nos arroja esta api status code: 200 está bien.
    print(r.text) #arroja la lista con dictionario de la api
    print(type(r.text))#verificamos el tipo
    categories = r.json()#convierte en formato json ó list
    for category in categories:
        print(category["name"])