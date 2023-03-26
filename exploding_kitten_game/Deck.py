# Name: Saurav Upadhyaya
# Assignment: Exploding Kittens Game
# Description: In this file, we are declaring all playing cards and cat cards as per the instructions provided. Cat cards are grouped separately so that it will take less time to search the cat 
# cards while finding matching pair of Cat Cards. here, depending upon the number of players, number of exploding kitten cards will be kept in the playing cards.



import random


class Deck:

    """
    This class represents a deck of cards for the game "Exploding Kittens".

    Attributes:

        all_cards (list): A list of strings representing all the cards in the deck, including Exploding Kittens, Defuse cards, and other special action cards.
        cat_cards (list): A list of strings representing the cat cards in the deck.
    Methods:

        init(self, num_of_kittens): Constructs a new Deck object with a given number of Exploding Kittens cards and initializes the all_cards and cat_cards attributes.
    """

    def __init__(self,num_of_kittens):
        self.all_cards = (["Exploding Kitten"] * num_of_kittens + ["Defuse"] * 6 + ["Skip"] * 4 + ["Attack"] * 4 + ["See the Future"] * 5 + ["Shuffle"] * 4 + 
                         ["Favor"] * 4 + ["Nope"] * 5 + ["Taco Cat"] * 4 +["Hairy Potato Cat"] * 4 + ["Beared Cat"] * 4 + ["Rainbow Ralphing Cat"] * 4 + ["Cattermelon"] * 4)
        self.cat_cards = ["Taco Cat", "Hairy Potato Cat", "Rainbow-Ralphing Cat", "Beard Cat","Cattermelon" ]