import requests

#vamos optener y leer la api así: 
def getCategories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)#vemos que estatus nos arroja esta api status code: 200 está bien.
    print(r.text) #arroja la lista con dictionario de la api
    print(type(r.text))#verificamos el tipo, en este es type String
    
    categories = r.json()#convierte el formato String a formato json ó list
    
    for category in categories:
        print(category["name"])#recorremos nuestro json y vemos los valores de las key "name".