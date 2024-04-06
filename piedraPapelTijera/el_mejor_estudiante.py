def calcular_promedio(estudiante):
    # Calcular el promedio de las notas del estudiante
    promedio = (estudiante["matematicas"] + estudiante["espanol"] + estudiante["ciencias"] + estudiante["literatura"] + estudiante["arte"]) / 5
    return promedio

def mejor_del_salon(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    # Calcular el promedio de cada estudiante
    promedio_estudiante1 = calcular_promedio(estudiante1)
    promedio_estudiante2 = calcular_promedio(estudiante2)
    promedio_estudiante3 = calcular_promedio(estudiante3)
    promedio_estudiante4 = calcular_promedio(estudiante4)
    promedio_estudiante5 = calcular_promedio(estudiante5)
    
    # Crear una lista de tuplas con el nombre y promedio de cada estudiante
    estudiantes = [
        (estudiante1["nombre"], promedio_estudiante1),
        (estudiante2["nombre"], promedio_estudiante2),
        (estudiante3["nombre"], promedio_estudiante3),
        (estudiante4["nombre"], promedio_estudiante4),
        (estudiante5["nombre"], promedio_estudiante5)
    ]
    
    # Encontrar el estudiante con el mejor promedio
    mejor_promedio = max(estudiantes, key=lambda x: (x[1], x[0].lower()))
    
    return mejor_promedio

# Solicitar al usuario que ingrese los datos de cada estudiante
estudiante1 = {
    "nombre": input("Ingrese el nombre del primer estudiante: "),
    "matematicas": float(input("Ingrese la nota de Matemáticas del primer estudiante: ")),
    "espanol": float(input("Ingrese la nota de Español del primer estudiante: ")),
    "ciencias": float(input("Ingrese la nota de Ciencias del primer estudiante: ")),
    "literatura": float(input("Ingrese la nota de Literatura del primer estudiante: ")),
    "arte": float(input("Ingrese la nota de Arte del primer estudiante: "))
}

estudiante2 = {
    "nombre": input("Ingrese el nombre del segundo estudiante: "),
    "matematicas": float(input("Ingrese la nota de Matemáticas del segundo estudiante: ")),
    "espanol": float(input("Ingrese la nota de Español del segundo estudiante: ")),
    "ciencias": float(input("Ingrese la nota de Ciencias del segundo estudiante: ")),
    "literatura": float(input("Ingrese la nota de Literatura del segundo estudiante: ")),
    "arte": float(input("Ingrese la nota de Arte del segundo estudiante: "))
}

estudiante3 = {
    "nombre": input("Ingrese el nombre del tercer estudiante: "),
    "matematicas": float(input("Ingrese la nota de Matemáticas del tercer estudiante: ")),
    "espanol": float(input("Ingrese la nota de Español del tercer estudiante: ")),
    "ciencias": float(input("Ingrese la nota de Ciencias del tercer estudiante: ")),
    "literatura": float(input("Ingrese la nota de Literatura del tercer estudiante: ")),
    "arte": float(input("Ingrese la nota de Arte del tercer estudiante: "))
}

estudiante4 = {
    "nombre": input("Ingrese el nombre del cuarto estudiante: "),
    "matematicas": float(input("Ingrese la nota de Matemáticas del cuarto estudiante: ")),
    "espanol": float(input("Ingrese la nota de Español del cuarto estudiante: ")),
    "ciencias": float(input("Ingrese la nota de Ciencias del cuarto estudiante: ")),
    "literatura": float(input("Ingrese la nota de Literatura del cuarto estudiante: ")),
    "arte": float(input("Ingrese la nota de Arte del cuarto estudiante: "))
}

estudiante5 = {
    "nombre": input("Ingrese el nombre del quinto estudiante: "),
    "matematicas": float(input("Ingrese la nota de Matemáticas del quinto estudiante: ")),
    "espanol": float(input("Ingrese la nota de Español del quinto estudiante: ")),
    "ciencias": float(input("Ingrese la nota de Ciencias del quinto estudiante: ")),
    "literatura": float(input("Ingrese la nota de Literatura del quinto estudiante: ")),
    "arte": float(input("Ingrese la nota de Arte del quinto estudiante: "))
}

# Encontrar al mejor estudiante y mostrar el resultado
mejor_estudiante = mejor_del_salon(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5)
print(f"El mejor estudiante se llama {mejor_estudiante[0]} y su promedio es: {mejor_estudiante[1]}")
