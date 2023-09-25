price = 100 #es una variable global

def increment():
    price = 200 #Esta variable es local de la función
    result = price + 10
    print(f"variable dentro de la función => {result}")
    return result

print(f"variable global => {price}")
price2 = increment()
print(f"variable que retorna de la función => {price2}")

