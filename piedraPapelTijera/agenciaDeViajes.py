def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):
    # Convertir la duración total del vuelo a segundos
    duracion_total_segundos = duracion_horas * 3600 + duracion_minutos * 60 + duracion_segundos
    
    # Convertir la hora de salida a segundos
    hora_salida_segundos = hora_salida * 3600 + minuto_salida * 60 + segundo_salida
    
    # Calcular la hora de llegada en segundos
    hora_llegada_segundos = hora_salida_segundos + duracion_total_segundos
    
    # Calcular horas, minutos y segundos de la hora de llegada
    horas_llegada = hora_llegada_segundos // 3600
    minutos_llegada = (hora_llegada_segundos % 3600) // 60
    segundos_llegada = hora_llegada_segundos % 60
    
    # Formatear la hora de llegada como cadena en el formato HH:mm:ss
    hora_llegada_str = f"{horas_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}"
    
    return hora_llegada_str

# Solicitar al usuario que ingrese los datos
hora_salida = int(input("Ingrese la hora de salida del vuelo: "))
minuto_salida = int(input("Ingrese el minuto de salida del vuelo: "))
segundo_salida = int(input("Ingrese el segundo de salida del vuelo: "))
duracion_horas = int(input("Ingrese la duración en horas del vuelo: "))
duracion_minutos = int(input("Ingrese la duración en minutos del vuelo: "))
duracion_segundos = int(input("Ingrese la duración en segundos del vuelo: "))

# Calcular la hora de llegada del vuelo e imprimir el resultado
hora_llegada = calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos)
print("Hora de llegada del vuelo:", hora_llegada)
