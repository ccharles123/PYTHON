#importa mos el zen de python, el cual es la filosofia en que se utiliza y construye python
#import this
'''
#importamos desde paquete el module1:
from paquete.module1 import func1, func2

print(func1())
print(func2())

#importamos desde paquete el module2:
from paquete.module2 import func3, func4
print(func3())
print(func4())
'''

#puedo ejecutar directamente la la variable URL, y debo importar en el init el module1 y el module2:
import paquete
print(paquete.url)
print(paquete.module1.func1())
print(paquete.module2.func3())