from deck import Deck
from hand import Hand
from utils import *

def main():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal initial cards
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Show player hands
    print("Player's hand:", ', '.join(str(card) for card in player_hand.cards))
    print("Player's hand value: ", player_hand.value)
    
    # Show dealer up card
    print("\nDealer's Up card: ", dealer_hand.cards[0])

    # Check for BJ
    playerBJ = checkBJ(player_hand)
    dealerBJ = checkBJ(dealer_hand)

    # Only allow game loop if there is no BJ
    if playerBJ and not dealerBJ:
        print("\nYou have Blackjack! :)")
        gameOn = False
    elif playerBJ and dealerBJ:
        print("Player and Dealer both have Blackjack, it is a push!")
        gameOn = False
    else:
        gameOn = True

    # Game loop starts here
    while gameOn:
        # 1. Players Turn
        playerBust = player_turn(player_hand, dealer_hand, deck)
        if playerBust:
            print("\nYou have busted. You Lose.")
        # 2. After players turn and they didn't bust, it is dealers turn
        print("\nNow for the dealer...")
        dealerBust = dealer_turn(dealer_hand, deck)

        # 3. Determine the winner and end the game
        if dealerBust and not playerBust:
            print("\nYou have won! :)")
            gameOn = False
        elif player_hand.value > dealer_hand.value and player_hand.value < 22:
            print("\nYou have won! :)")
            gameOn = False
        elif player_hand.value == dealer_hand.value:
            print("\nIt's a push!")
            gameOn = False
        else:
            print("\nDealer Wins :(")
            gameOn = False


if __name__ == "__main__":
    main()