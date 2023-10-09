list1 = list()#[]
list2 = ["t", 25, "cat", 3.1234]#['t', 25, 'cat', 3.1234
list3 = [number**2 for number in range(1, 100, 3)]#[1, 16, 49, 100, 169, 256, 361, 484, 625, 784, 961, 1156, 1369, 1600, 1849, 2116, 2401, 2704, 3025, 3364, 3721, 4096, 4489, 4900, 5329, 5776, 6241, 6724, 7225, 7744, 8281, 8836, 9409]

print(list1)
print(list2)
print(list3)

# A diferencia de las tuplas, las listas son mutables, lo que significa que puedes agregar, 
# eliminar o modificar elementos después de crear la lista. Esto es esencial cuando necesitas 
# actualizar o cambiar datos durante la ejecución de un programa.

#ejemplo de list => listado de estudiantes de un salon:

listEstudiantes5A = [
    "Mariana Hernadez", 
    "Camila Rodriguez", 
    "Carlos Fernandez",
    "Edimer Villarreal", 
    "Betty Lopez", 
    "Marlene Cueto"
    ]