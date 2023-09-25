import random

# Juego Piedra, Papel ó Tijeras



name = input("Bienvenido al juego Pierda papel o Tijera.! por favor ingresa tu nombre => ").upper()
print(f"listo {name}, comencemos el juego.!")

def chooseOptions(name):
    options = ("piedra", "papel", "tijera")
    userOptions = input(f"{name} escoge tu opción: piedra, papel ó tijera: ").lower()
    
    if not userOptions in options:
        print("Opcion no es valida")
        #continue
        return None, None

    computerOption = random.choice(options)

    print(f"{name} Option => {userOptions}")
    print("Computer Option=> ", computerOption)
    return userOptions, computerOption

def checkRules(userOptions, computerOption, userWins, computerWins, empate):
    if (not(userOptions == None)) & (not(computerOption == None)) & (userOptions == computerOption):
        print("¡EMPATE!")
        empate += 1
        
    elif userOptions == "piedra":
        if computerOption == "tijera":
            print("Piedra gana a Tijera")
            print("¡GANASTE!")
            userWins +=1
        else:
            print("Piedra pierde con Papel")
            print("¡PERDISTE!")
            computerWins += 1

    elif userOptions == "papel":
        if computerOption == "piedra":
            print("Papel gana a Piedra")
            print("¡GANASTE!")
            userWins +=1
        else:
            print("Papel pierde con Tijera")
            print("¡PERDISTE!")
            computerWins += 1
            
    elif userOptions == "tijera":
        if computerOption == "papel":
            print("Tijera gana a Papel")
            print("¡GANASTE!")
            userWins +=1
        else:
            print("Tijera pierde con Piedra")
            print("¡PERDISTE!")
            computerWins += 1
    return userWins, computerWins, empate

def wins(name, userWins, computerWins, empate):
    if userWins == 2:
        
        print("*********** Ganaste EL JUEGO! ************")
        print("********** RESULTADO DEL JUEGO **********")
        print(f"{name} => {userWins}")
        print(f"COMPUTADORA => {computerWins}")
        print(f"EMPATE => {empate}")
        print("*" * 43)
        return True
    
    if computerWins == 2:
        
        print("*********** Perdiste EL JUEGO! ***********")
        print("********** RESULTADO DEL JUEGO **********")
        print(f"{name} => {userWins}")
        print(f"COMPUTADORA => {computerWins}")
        print(f"EMPATE => {empate}")
        print("*" * 43)  
        return True 

def runGame():
    userWins = 0
    computerWins = 0
    empate = 0
    round = 1
    gameOver = False
    
    while not gameOver:
        print("*" * 30)
        print(f"********** ROUND {round} ***********")
        print("*" * 30)
        print("********** PUNTUACIÓN ***************")
        print(f"{name} => {userWins}")
        print(f"COMPUTADORA => {computerWins}")
        print(f"EMPATE => {empate}")
        print("*" * 43)

        userOptions, computerOption = chooseOptions(name)
        userWins, computerWins, empate = checkRules(userOptions, computerOption, userWins, computerWins, empate)
        gameOver = wins(name, userWins, computerWins, empate)
        round += 1    

runGame()