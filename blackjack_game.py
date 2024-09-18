from deck import Deck
from hand import Hand
from utils import *

def main():
    # Initial Game
    deck = Deck()
    gameOfBJ(deck)
    reset = 1
    
    while reset == 1:
        # Ask user if they would like to keep playing
        playAgain = input("Would you like to play again? (Yes/No): ")

        if playAgain == "Yes":
            deck.check_for_reshuffle()
            gameOfBJ(deck)
        elif playAgain == "No":
            reset = 0
        


if __name__ == "__main__":
    main()