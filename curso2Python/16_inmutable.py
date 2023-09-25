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

# Vamos a enfocarnos en no modificar eñ array original:

def addTaxes(item):
    item["taxes"] = item["price"] * .15 
    return item

newItems = list(map(addTaxes, items))
print("New List")
print(newItems)
print("Old List")
print(items)