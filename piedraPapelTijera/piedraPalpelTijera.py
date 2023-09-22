import random

# Juego Piedra, Papel ó Tijeras
options = ("piedra", "papel", "tijera")
round = 1
userWins = 0
computerWins = 0
empate = 0
name = input("Bienvenido al juego Pierda papel o Tijera.! por favor ingresa tu nombre => ").upper()
print(f"listo {name}, comencemos el juego.!")

while True:
    
    print("*" * 30)
    print(f"********** ROUND {round} ***********")
    print("*" * 30)
    
    
    userOptions = input("piedra, papel ó tijera: ").lower()

    if not userOptions in options:
        print("Opcion no es valida")
        continue

    computerOption = random.choice(options)

    print("User Option => ", userOptions)
    print("Computer Option=> ", computerOption)

    if userOptions == computerOption:
        print("Empate")
        empate += 1
        
    elif userOptions == "piedra":
        if computerOption == "tijera":
            print("Piedra gana a Tijera")
            print("Ganaste")
            userWins +=1
        else:
            print("Piedra pierde con Papel")
            print("Perdiste")
            computerWins += 1

    elif userOptions == "papel":
        if computerOption == "piedra":
            print("Papel gana a Piedra")
            print("Ganaste")
            userWins +=1
        else:
            print("Papel pierde con Tijera")
            print("Perdiste")
            computerWins += 1
            
    elif userOptions == "tijera":
        if computerOption == "papel":
            print("Tijera gana a Papel")
            print("Ganaste")
            userWins +=1
        else:
            print("Tijera pierde con Piedra")
            print("Perdiste")
            computerWins += 1
    
    if userWins == 2:
        
        print("*********** Ganaste EL JUEGO! ************")
        print("********** RESULTADO DEL JUEGO **********")
        print(f"{name} => {userWins}")
        print(f"COMPUTADORA => {computerWins}")
        print(f"EMPATE => {empate}")
        print("*" * 43)
        break
    
    if computerWins == 2:
        
        print("*********** Perdiste EL JUEGO! ***********")
        print("********** RESULTADO DEL JUEGO **********")
        print(f"{name} => {userWins}")
        print(f"COMPUTADORA => {computerWins}")
        print(f"EMPATE => {empate}")
        print("*" * 43)
        break
    
    print("********** RESULTADO DE LA RONDA **********")
    print(f"{name} => {userWins}")
    print(f"COMPUTADORA => {computerWins}")
    print(f"EMPATE => {empate}")
    print("*" * 43)
    
    round += 1