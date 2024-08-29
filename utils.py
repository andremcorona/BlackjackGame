from deck import Deck
from hand import Hand

def player_turn(player_hand, dealer_hand, deck):
    while player_hand.value < 22:
        print("\nWould you like to Hit or Stand:")
        playerChoice = input("")
        # If user hits
        if playerChoice == "Hit":
            player_hand.add_card(deck.deal())
            print("\nPlayer's hand:", ', '.join(str(card) for card in player_hand.cards))
            print("Player's hand value:", player_hand.value)
            if player_hand.value > 21:
                return True
        # If user stands
        elif playerChoice == "Stand":
            return False
        # Make sure users enter either hit or stand
        else:
            print("\nYou may only enter either Hit or Stand")
    return False

def dealer_turn(dealer_hand, deck):
    # Show dealers entire hand
    print("Dealer's hand:", ', '.join(str(card) for card in dealer_hand.cards))
    print("Dealer's hand value:", dealer_hand.value)

    # Dealer stands on 17 and above
    while dealer_hand.value < 17:  
        dealer_hand.add_card(deck.deal())
        print("")
        print("Dealer's hand:", ', '.join(str(card) for card in dealer_hand.cards))
        print("Dealer's hand value:", dealer_hand.value)
        # Dealer bust on any value above 21
        if dealer_hand.value > 21:
            print("/nDealer has busted.")
            return True
    return False

def checkBJ(hand):
    if hand.value == 21:
        return True
    else:
        return False