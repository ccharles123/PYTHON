text = "Ella sabe programar en Python"

# IN: Informa si una cadena de texto está dento de una variable
"""
print("Javascript" in text)
print("Python" in text)

if "Python" in text:
    print("Elegiste bien")
else:
    print("Tambien elegiste bien") 
"""
# Tamaño de un String con len te dice el tamaño incluyendo los espacios

size = len(text)
print (size)

# Pasar todo el texto a MAYUSCULA .upper()
print(text)
print(text.upper())

# Pasar todo el texto a MINUSCULA .lower()
print(text.lower())

#cuantas veces aparece una letra en especifico .count()
print(text.count("a"))

# Pasa caracteres que esté en MINUSCULA a MAYUSCULA y MAYUSCULA a MINUSCULA .swapcase()
print(text.swapcase())

# Te dice si una cadena de string inicia con el string que le coloques .startswith(), te devuelve un boolen
print(text.startswith("Ella"))

# Te dice si una cadena de string finaliza con el string que le coloques .endswith(), te devuelve un boolen
print(text.endswith("Java"))

# Puedes reemplazar una cadena de texto por otra .replace()
print(text.replace("Python", "Java"))

texto2 = "este es un titulo"
print(texto2)

# Coloca el primer caracter en mayuscula .capitalase()
print(texto2.capitalize())

# coloca el inicio de cada una de las palabras qjue está en esa cadena de texto en mayuscula .title()
print(texto2.title())

# Nos indica si este texto es un digito isdigit(), arroja un boolean
print(texto2.isdigit())
print("12345".isdigit())