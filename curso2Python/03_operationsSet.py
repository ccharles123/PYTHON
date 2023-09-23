setA = {"colombia", "bolivia", "mexico"}
setB = {"bolivia", "perú"}
setD = {"brasil", "colombia"}

# Union: Une dos conjuntos sin repetir los elementos en común:
setC = setA.union(setB, setD)
print(setC)
print(setA | setB) # se puede hacer con este operador
print(setA | setB | setD)

#Interseccion: muestra los elementos en común:
setC= setA.intersection(setB)
print(setC)
print(setA & setB)

#Diferencia: muestra los elementos del primer conjunto removiendo los que coinciden con el segundo, practicamante una resta
setC= setA.difference(setB)
print(setC)
print(setA - setB)

#diferencia simetrica: resultado de un conjunto con la union de los dos sin los elementos que son comunes:
setC= setA.symmetric_difference(setB)
print(setC)
print( setA ^ setB)
