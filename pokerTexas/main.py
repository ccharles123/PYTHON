# main.py

import pokerTexas

if __name__ == "__main__":
    try:
        num_players = int(input("¿Cuántos jugadores desean jugar (hasta 3)? "))
        if num_players < 1 or num_players > 3:
            raise ValueError("Número de jugadores no válido.")
        
        pokerTexas.main(num_players)
    except ValueError as e:
        print(f"Error: {e}. Debes ingresar un número válido de jugadores (1-3).")
