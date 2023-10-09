from array_1 import Array

class array2d():
    def __init__(self, rows, columns, fill_values=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_values)
    #definimos la altura:
    def get_height(self):
        return len(self.data)
    #definimos el ancho:
    def get_width(self):
        return len(self.data[0])
    
    #obetner un elemento en particular:
    def __getitem__(self, index):
        return self.data[index]
    
    #respesentacion en string de alguno de esos valores:
    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)

#creamos la instancia ó array2D 3x3 y luego lo imprimimos:
matrix = array2d(3, 3)
print(matrix)

#agregamos valores a nuestra matrix o array2D
for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = row * column

print(matrix)

'''pongamos a prueba sus metodos'''
#obtener altura:
print(matrix.get_height())

#obtener ancho:
print(matrix.get_width())

#obtener alguno de sus item deben ingresar .__getitem__(row)[column]:
print(matrix.__getitem__(2)[1])

#obtener la representación en string:
print(matrix.__str__())