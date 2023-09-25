items = [
    {
        "producto" : "camisa",
        "price" : 100      
    },
    {
        "producto" : "camiseta",
        "price" : 80
    },
    {
        "producto" : "pantalon",
        "price" : 150
    }
]

#sacar los valores de los dic internos del array:
price = list(map(lambda  item: item["price"],items))
product = list(map(lambda  item: item["producto"],items))
print(product)
print(price)

#map no modifica el estado del array original, crea uno nuevo
print(items)


#agregar un item nuevo llamado taxes para calcular el impueto por el precio:

def addTaxes(item):
    item["taxes"] = item["price"] * .15 
    return item

newItems = list(map(addTaxes, items))
print(newItems)

#luego de la función, si se modifica el estado del array original:
print(items)