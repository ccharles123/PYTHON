def movimiento_robot(orientacion_actual, giro_01, giro_02, giro_03):
    orientaciones = ['N', 'E', 'S', 'W']  # Lista de orientaciones posibles
    
    # Obtener el índice de la orientación actual en la lista de orientaciones
    indice_orientacion = orientaciones.index(orientacion_actual)
    
    # Aplicar los giros uno por uno
    for giro in [giro_01, giro_02, giro_03]:
        if giro == 'L':  # Girar a la izquierda
            indice_orientacion = (indice_orientacion - 1) % 4
        elif giro == 'R':  # Girar a la derecha
            indice_orientacion = (indice_orientacion + 1) % 4
        elif giro == 'H':  # Dar media vuelta
            indice_orientacion = (indice_orientacion + 2) % 4
    
    # Obtener la orientación final del robot
    orientacion_final = orientaciones[indice_orientacion]
    
    return orientacion_final

# Pedir al usuario la posición inicial del robot y los giros
orientacion_actual = input("Ingrese la orientación actual del robot (N, S, E, W): ")
giro_01 = input("Ingrese el primer giro (L, R, H, .): ")
giro_02 = input("Ingrese el segundo giro (L, R, H, .): ")
giro_03 = input("Ingrese el tercer giro (L, R, H, .): ")

# Calcular la orientación final del robot e imprimir el resultado
orientacion_final = movimiento_robot(orientacion_actual, giro_01, giro_02, giro_03)
print("La orientación final del robot es:", orientacion_final)
