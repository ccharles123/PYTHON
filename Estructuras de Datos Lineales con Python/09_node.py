#vamos hacer nuestro primer node:
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = None
node2 = Node("A", None)#tiene un valor pero no se conecta a ningun nodo
node3 = Node("B", node2)#tiene un valor pero se conecta al nodo2

#podemos llamarlo con su reference en memoria:
print(node2)

#podemos llamar su valor:
print(node2.data)
print(node3.data)

#podemos ver a donde nos lleva el node3 en representacion de memoria:
print(node3.next)
#podemos ver el valor a donde nos lleva el node3 en representacion de memoria:
print(node3.next.data)
#podemos reasignar valores a nuestros nodos y que apunte a otro node, por ejemplo:
node1 = Node("C", node3)
print(node1.data)
print(node1.next.data)

#vamos a crear una serie de nodos:
print("creacion de un nodo iterativo:")
head = None
for count in range(1, 5):
    head = Node(count, head)

while head != None:
    print(head.data)
    head = head.next


