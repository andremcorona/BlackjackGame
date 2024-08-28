from deck import Deck
from hand import Hand

def main():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal initial cards
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Game loop would go here (Hit/Stand, check for win/loss, etc.)
    # Show hands
    print("Player's hand:", ', '.join(str(card) for card in player_hand.cards))
    print("Player's hand value:", player_hand.value)

    print("Dealer's hand:", ', '.join(str(card) for card in dealer_hand.cards))
    print("Dealer's hand value:", dealer_hand.value)
    
if __name__ == "__main__":
    main()