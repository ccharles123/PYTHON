def message_creator(text):
# Escribe tu solución 👇

    respuestas = {
    'computadora' : "Con mi computadora puedo programar usando Python", 
    'celular' : "En mi celular puedo aprender usando la app de Platzi", 
    'cable' : "¡Hay un cable en mi bota!"
    }

    if text in respuestas.keys():
        return respuestas[text]
    else: 
        return'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)

# Otra forma de hacerlo:
def message_creator(text):
    
# Escribe tu solución 👇
    options = ("computadora", "celular", "cable")
    if not text in options:
        response = "Artículo no encontrado"
    if text == "computadora":
        response = "Con mi computadora puedo programar usando Python"
    elif text == "celular":
        response = "En mi celular puedo aprender usando la app de Platzi"
    elif text == "cable":
        response = "¡Hay un cable en mi bota!"
    return response

text = 'computadora'
response = message_creator(text)
print(response)