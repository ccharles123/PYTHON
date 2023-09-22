setCountries = {"colombia", 'mexico', 'argentina', "colombia"}

#tamaño del conjunto con el metodo "len(nombre del conjunto)":
print(len(setCountries)) #muestra el tamaño del conjunto eliminando los objetos repetidos

#puedo pregunta por un elemento en especifico, devuelve un boolean:
print("colombia" in setCountries)
print("perú" in setCountries)

# adicionar un elemento al conjunto, si lo agrego varias veces solo me deja agregarlo una sola vez:
setCountries.add("perú")
print(setCountries)

# UpDate: actualizar mi conjunto agregando un subconjunto a mi conjunto con el .update({subconjunto a agregar al conjunto}):
setCountries.update({"venezuela", "brasil"})
print(setCountries)

# Delete: Eliminar elemento del conjunto con el metodo .remove("nombre del elemento a elimiar"), 
# en el caso de no existir el elemento a eliminar arroja un error:
setCountries.remove("colombia")
print(setCountries)

# Otra forma de eliminar .discard("nombre del elemento a elimiar"), 
# en el caso de no existir el elemento a eliminar no pasa nada, nisiquiera enviar un error:
setCountries.discard("chile")
print(setCountries)#no encuentra el elemento pero aún así lo imprime sin generar un error