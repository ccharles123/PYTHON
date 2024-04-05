def calcular_cambio(cambio):
    monedas_500 = cambio // 500
    cambio %= 500
    
    monedas_200 = cambio // 200
    cambio %= 200
    
    monedas_100 = cambio // 100
    cambio %= 100
    
    monedas_50 = cambio // 50
    
    return f"{monedas_500} de 500, {monedas_200} de 200, {monedas_100} de 100, {monedas_50} de 50"

# Solicitar al usuario el valor del dinero ingresado por el comprador y el valor del producto
dinero_comprador = int(input("Ingrese el valor del dinero entregado por el comprador en pesos: "))
valor_producto = int(input("Ingrese el valor del producto en pesos: "))

# Calcular el cambio
cambio = dinero_comprador - valor_producto

# Mostrar el mensaje con la cantidad de monedas de cada denominación que se deben entregar como cambio
print(f"El cambio es de {cambio} pesos: {calcular_cambio(cambio)}")