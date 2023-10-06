import random

def main():
    limiteMayor = int(input("Inserta el numero del limite mayor del rango => "))
    limiteMenor = int(input("Inserta el numero del limite menor del rango => "))
    numeroOculto = random.randint(limiteMenor, limiteMayor)
    numeroUsuario = int(input(f"Inserta un numero entre {limiteMenor} a {limiteMayor} y veamos si adivinas => "))
    intentos = 0
    
    while True:
        intentos +=1
        
        if numeroOculto < numeroUsuario:
            print("Intenta con numero menor")
            numeroUsuario = int(input(f"llevas {intentos} intentos, ingresar un nuevo numero entre {limiteMenor} y {limiteMayor} => "))
        elif numeroOculto > numeroUsuario:
            print("Intenta con numero mayor")
            numeroUsuario = int(input(f"llevas {intentos} intentos, ingresar un nuevo numero entre {limiteMenor} y {limiteMayor} => "))
        else:
            print("¡Adivinaste!")
            print(f"Lo hiciste en {intentos} intentos")
            break
        

if __name__ == "__main__":
    main()
