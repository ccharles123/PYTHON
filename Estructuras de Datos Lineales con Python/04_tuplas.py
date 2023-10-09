# Las tuplas son objetos inmutables, lo que significa que una vez que se crea una tupla, 
# sus elementos no pueden modificarse. Esto puede ser útil cuando deseas asegurarte de 
# que los datos no cambien accidentalmente.

tuple1 = ()
tuple2 = (1234, 3456, 4532)
tuple3 = "Mariana", "Edimer", "Bombon"

print(tuple1)#()
print(tuple2)#(1234, 3456, 4532)
print(tuple3)#('Mariana', 'Edimer', 'Bombon')

#ejemplo de tuple => nombre de paises de Sur America:

tuplePaisesSurAmerica = (
    "Argentina",
    "Bolivia",
    "Brasil",
    "Chile",
    "Colombia",
    "Ecuador",
    "Guyana",
    "Paraguay",
    "Perú",
    "Surinam",
    "Uruguay",
    "Venezuela"
)

print(tuplePaisesSurAmerica)
