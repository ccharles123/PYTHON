class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, newItem):
        self.items[index] = newItem

'''metodos propios de python'''
#print("metodos propios de python")
#hacer un array de 5 elementos:
menu = Array(5)
#print(len(menu))#5
#print(menu) #[None, None, None, None, None]

#cambiar los elementos de mi array por un contador:
for i in range(len(menu)):
    menu[i] = i + 1

#imprimir las siguientes posiciones despues del cambio del contador:
#print(menu[0])#1
#print(menu[4])#5

#recorrer mi array:
#for option in menu:
    #print(menu[option -1]) #1 2 3 4 5

#'''metodos propios de nuestra clase array'''
#conocer la longitud:
#print("metodos propios de nuestra clase array")
#print(menu.__len__())#5
#representacion de dichos elementos:
#print(menu.__str__())#[1, 2, 3, 4, 5]
#llamemos el metodo iterador su referencia en memoria:
#print(menu.__iter__())#<list_iterator object at 0x000002859835B760>
#veamos que elemento hay deacuerdo a su indice:
#print(menu.__getitem__(2))#3
#agregar valores en el indice que quiero con el metodo setitem:
menu.__setitem__(2, 100)
#print(menu.__getitem__(2))#100
