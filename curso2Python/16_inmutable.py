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

# Vamos a enfocarnos en no modificar el array original (items):

def addTaxes(item):
    #generamos una copia del array original y a ese le realizamos la modificacion:
    newArray = item.copy()
    newArray["taxes"] = newArray["price"] * .15 
    return newArray

newItems = list(map(addTaxes, items))
print("New List")
print(newItems)
print("Old List")
print(items)