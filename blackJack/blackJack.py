import random

def deal_card():
    """Genera una carta aleatoria del mazo."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(hand):
    """Calcula el valor de la mano del jugador o del crupier."""
    score = 0
    ace_count = hand.count('A')
    
    for card in hand:
        if card in 'JQK':
            score += 10
        elif card == 'A':
            score += 11
        else:
            score += int(card)
    
    # Ajusta el valor del As si el puntaje es mayor a 21
    while ace_count > 0 and score > 21:
        score -= 10
        ace_count -= 1
    
    return score

def play_game():
    """Función principal para jugar Blackjack."""
    partidas_totales = 0
    partidas_ganadas = 0
    partidas_perdidas = 0
    
    while True:
        partidas_totales += 1
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]
        
        while True:
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            
            print(f"Tu mano: {player_hand}, Puntuación: {player_score}")
            print(f"Carta del crupier: {dealer_hand[0]}")
            
            if player_score == 21 and len(player_hand) == 2:
                print("¡Blackjack! ¡Ganaste!")
                partidas_ganadas += 1
                break
            elif player_score > 21:
                print("¡Te pasaste de 21! ¡Perdiste!")
                partidas_perdidas += 1
                break
            
            action = input("¿Quieres tomar otra carta? (s/n): ").lower()
            if action == 's':
                player_hand.append(deal_card())
            else:
                while dealer_score < 17:
                    dealer_hand.append(deal_card())
                    dealer_score = calculate_score(dealer_hand)
                
                print(f"Mano del crupier: {dealer_hand}, Puntuación: {dealer_score}")
                
                if dealer_score > 21:
                    print("El crupier se pasó de 21. ¡Ganaste!")
                    partidas_ganadas += 1
                elif dealer_score > player_score:
                    print("El crupier gana. ¡Perdiste!")
                    partidas_perdidas += 1
                elif dealer_score < player_score:
                    print("¡Ganaste!")
                    partidas_ganadas += 1
                else:
                    print("Empate.")
                
                break
        
        print(f"Total partidas => {partidas_totales}, Partidas Ganadas => {partidas_ganadas}, Partidas Perdidas => {partidas_perdidas}")
        
        continuar = input("¿Quieres continuar jugando? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    play_game()

