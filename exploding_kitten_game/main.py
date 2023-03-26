# Name: Saurav Upadhyaya
# Assignment: Exploding Kittens Game
# Description: Here, the number of players are provided ensuing they are within the allowed range and player names are collected, and then player objects are created. At first, all kitten cards 
# and defuse cards are kept aside from all cards and for each player 7 cards are drawn. Also, one defuse card is given to each player. So, each player will have 8 cards in their hands before they
# start playing the game. Depending upon the number of players, number of exploding kitten cards are placed back to the playing cards ( 1 fewer than the number of people playing). To determine the
# number of defuse cards to put back in the deck, logic is applied in a way when there are only 2 to 3 players, only 2 of the extra Defuse Cards are kept back into the deck. Remove the remaining 
#D efuse Cards from the game. Then, the player starts playing the game as play_game fucntion of Player Class is called. In this way, all other players get chance to play in their turn. If one wants
# to replay the game, they can do that as well.


# Code goes below this line

from Deck import Deck
from Player import Player
import sys
import random

def main():
    """
        Starts the Exploding Kittens game and runs the game loop until it ends.
        Asks for the number of players, creates the player objects, and deals
        the cards to the players. Also handles playing the game and asking
        if the players want to play again.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Raises
        ------
        Exception
            If there are not enough cards in the deck to deal to all players.
    """
    players_list = []
    while True:
        try:
            num__of_players = int(input("How many players? (2-5) "))
            # Ensure the number of players is within the allowed range
            if num__of_players < 2 or num__of_players > 5:
                print("Please enter a number between 2 and 5.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    num_of_kittens = 1 if num__of_players == 2 else 2 if num__of_players == 3 else 3 if num__of_players == 4 else 4
    deck = Deck(num_of_kittens)
    # collect player names and create player objects
    for i in range(num__of_players):
        name = ""
        while not name:
            try:
                name = input("Enter the Name of player: ")
                if not name:
                    print("Name cannot be empty.")
            except KeyboardInterrupt:                     
                print("Exiting the game.")
                sys.exit(0)
        players_list.append(Player(name, players_list, deck.all_cards, deck.cat_cards))

    if len(deck.all_cards) < len(players_list) * 5: raise Exception("Not enough cards in all_cards to deal to all players.")

    # Count the number of Defuse Cards in the deck
    num_of_defuse_cards = deck.all_cards.count("Defuse")

    # Remove all Defuse Cards and Exploding Kittens from the deck and set them aside
    newDeck= [card for card in deck.all_cards if card not in ["Defuse", "Exploding Kitten"]]
    random.shuffle(newDeck)
    # deal 7 cards face down to each player with 1 defuse card for each player
    for i in range(len(players_list)):
        for j in range(7):
            card = newDeck.pop()
            players_list[i].hand.append(card)
        players_list[i].hand.append("Defuse")  

    #When there are only 2 to 3 players, put only 2 of the extra Defuse Cards back into the deck. Remove the remaining Defuse Cards from the game
    num__of_defuse_cards_back_into_deck = 2 if len(players_list) in (2, 3) else num_of_defuse_cards - len(players_list)

    #Insert enough Exploding Kittens back into the deck so that there is 1 fewer than the number of people playing and defuse cards as well
    deck.all_cards= newDeck + ["Exploding Kitten"] * num_of_kittens + ["Defuse"] * num__of_defuse_cards_back_into_deck
    random.shuffle(deck.all_cards)
    players_list[0].play_game()
    
    while True:
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == 'y': main()
        else: 
            print("---------------------------------------------------------------------")
            print("Thank you for playing. Hope you enjoyed the Exploding Kitten Game.")
        break


if __name__ == "__main__":
    main()
