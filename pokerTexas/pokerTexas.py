import random

def deal_cards(num_players):
    """Reparte dos cartas aleatorias a cada jugador, incluyendo la computadora."""
    deck = create_deck()
    hands = []
    
    for _ in range(num_players + 1):  # +1 para incluir la computadora
        hand = [deck.pop(random.randint(0, len(deck) - 1)) for _ in range(2)]
        hands.append(hand)
    
    return hands

def create_deck():
    """Crea una baraja de cartas."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def main(num_players):
    hands = deal_cards(num_players)
    
    for i, hand in enumerate(hands):
        player_name = f"Jugador {i + 1}" if i < num_players else "Computadora"
        print(f"{player_name} - Mano:")
        for card in hand:
            print(f"{card['rank']} of {card['suit']}")

if __name__ == "__main__":
    try:
        num_players = int(input("¿Cuántos jugadores desean jugar (hasta 3)? "))
        if num_players < 1 or num_players > 3:
            raise ValueError("Número de jugadores no válido.")
        
        main(num_players)
    except ValueError as e:
        print(f"Error: {e}. Debes ingresar un número válido de jugadores (1-3).")

