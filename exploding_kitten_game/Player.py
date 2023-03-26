# Name: Saurav Upadhyaya
# Assignment: Exploding Kittens Game
# Objective: To be last player standing and win the Game. 
# Description: Players take turns drawing cards from a deck and trying to avoid the exploding kitten cards. They can take certain actions on the drawn cards or cards that are in their hands. For that,
# handler methods are defined to perform actions as per the card. Also, it has "play game" method where logics for each cards are defined and players get chance to draw and play cards. Here, 
# discarded pile is created, where cards are added whenever any action cards are utilized or any cards are played by the players either playing defuse card to avoid dying if player draws exploding
# kitten etc. Here, after playing defuse card, player can place the exploding kitten anywhere in the deck. 
# The program keeps track of each player's hand and the remaining cards in the deck.
# The game ends when there is only single player left or if both the playing deck and discarded pile is empty. This occurs when all the players have gone through the entire deck without drawing 
# an Exploding Kitten card or have defused all the Exploding Kitten cards, and all the other special cards have been played as well. At this point, the game is considered to be over, and there are
# no more cards left to draw. This can be handled if initially instead of giving 7 cards to each player, few cards are distributed depending upon the number of players. 

# Note:Here, I got confused whether to show the cards present in each players hand while playing as it may not be more interesting to play if one already knows which player has which cards 
# and they can request that card during play while playing favor and attack cards. So, I am just hiding it to make it more natural play. It would be fine to share cards present on each players 
# hand if a game would have been played on individual machine and no one can see cards of other's hand.  


import random

class Player:

    """
    A class used to represent a player in the Exploding Kittens game.

    ...

    Attributes
    ----------
        name : str
            the name of the player
        lives : int
            the number of lives the player has (default 2)
        discard_pile : list
            the pile of discarded cards
        hand : list
            the player's hand of cards
        players : list
            a list of all players in the game
        current_player_index : int
            the index of the current player in the list of players
        current_player : Player
            the current player
        cat_cards : int
            the number of Exploding Kitten cards in the game
        defuse_index : int
            the index of the Defuse card in the player's hand
        all_cards : list
            a list of all the cards in the game
    """


    def __init__(self, name, players, all_cards, cat_cards):
        """
        Parameters:
            name: str
                The name of the players.
            players: list
                A list of player objects.
            all_cards: list
                A list of all the cards in the deck.
            cat_cards: list
                A list of all the possible categories to cat cards for.
        """
    
        self.name = name
        self.lives = 2
        self.discard_pile = []
        self.hand = []
        self.players = players
        self.current_player_index = 0
        self.current_player = None
        self.cat_cards = cat_cards
        self.defuse_index = 0
        self.all_cards = all_cards
        self.previous_card = None
 

    def give_card(self):
        '''
        Handles the situation to give card if there is at least one card in hand
        '''
        return None if len(self.hand) == 0 else self.hand.pop(random.randint(0, len(self.hand) - 1))

    def add_card(self, card):
        '''
        Appends card to player's hand once they draw card
        '''
        self.hand.append(card)

    def draw_card(self):
        '''
        Checks if cards are available in deck and discarded pile. If not, message is displayed. Otherwise, returns the drawn card
        '''
        if not self.all_cards:
            if not self.discard_pile:
                message = "There are no cards left to draw. The game ended in a Draw."
                print(message)
                return None
            random.shuffle(self.discard_pile)
            self.all_cards = self.discard_pile
            self.discard_pile = []

        random.shuffle(self.all_cards)
        drawn_card = self.all_cards.pop()
        return drawn_card
      

    def shuffle_discard_pile(self):
        '''
        Shuffles the discared pile
        '''
        random.shuffle(self.discard_pile)

    def defuse_card_with_player(self):
        '''
        Handles the case when the player has a Defuse card when an Exploding Kitten card is drawn
        Handle each placement choice to place the exploding kitten
        '''
        self.defuse_index = self.current_player.hand.index("Defuse")
        self.current_player.hand.pop(self.defuse_index)
        placement_choice = input("You have defuse card in hand. How would you like to place the Exploding Kitten?\n1) On top of the deck\n2) Randomly in the deck\n3) On a specific index\nEnter choice (1/2/3): ")
        # Place on top
        if placement_choice == '1': self.all_cards.insert(0, "Exploding Kitten")  
        # Calculate random index and placing over there
        elif placement_choice == '2': self.all_cards.insert(random.randint(0, len(self.all_cards)), "Exploding Kitten") 
        # Place at specified index 
        elif placement_choice == '3':
            index_choice = int(input("Enter the index where you want to place the Exploding Kitten (0 to {}): ".format(len(self.all_cards))))
            self.all_cards.insert(index_choice, "Exploding Kitten")
        else:
            print("Invalid choice. Exploding Kitten will be placed randomly.")
            self.all_cards.insert(random.randint(0, len(self.all_cards)), "Exploding Kitten") 

        print("You played a Defuse card and put the Exploding Kitten back in the deck.")
        self.discard_pile.append("Defuse")
        self.shuffle_discard_pile()

    def defuse_card_not_with_player(self):
        '''
        Handles the case when the player does not have a Defuse card when an Exploding Kitten card is drawn.
        Removes the player from the players group.
        '''
        print("Unfortunately, You don't have Defuse card to save you. You just took out Exploding Kitten card. You are out of Game!")
        self.discard_pile.append("Exploding Kitten")
        self.shuffle_discard_pile()
        self.players.remove(self.current_player)
        self.current_player_index -= 1

    def exploding_kitten__card_handler(self):
        '''
        Determines how to handle an Exploding Kitten card being drawn.
        Checks if Defuse card is with player or not. Calls the respective functions accordingly.
        '''
        self.defuse_card_with_player() if "Defuse" in self.current_player.hand else self.defuse_card_not_with_player()

    def defuse_card_handler(self, drawn_card):
        '''
        Handles the case when the player draws a Defuse card

        Parameter:
            drawn_card: str
                The card that was drawn from the deck.
        '''
        print("You picked up a defuse card.")

        if "Exploding Kitten" in self.current_player.hand:
            print("You have an exploding kitten! Choose a card to defuse it: ")

            self.current_player.hand.remove("Exploding Kitten")
            self.all_cards.insert(
                random.randint(0, len(self.all_cards)), "Exploding Kitten"
            )
            print("You defused the kitten! Your turn continues.")
            self.discard_pile.append("Defuse")
            self.shuffle_discard_pile()
        else:
            print("Exploding Kitten card is not in your hand!")
           

    def attack_card_handler(self, drawn_card):
        '''
        Handles the case when the player draws a Attack card. 
        Checks and handles if player played Skip card as a defense to Attack Card.
        Parameter:
            drawn_card: str
                The card that was drawn from the deck.
        '''
        print("You attacked the next player! They must draw two cards.")
        next_player_index = (self.current_player_index + 1) % len(self.players)
        for i in range(2):
            if self.all_cards:
                drawn_card = self.all_cards.pop()
                self.players[next_player_index].hand.append(drawn_card)
                print(self.players[next_player_index].name + " drew a " + drawn_card + ".")
            if not self.all_cards:
                # Shuffle the discard pile and make it the new all_cards
                self.shuffle_discard_pile()
                self.all_cards = self.discard_pile
                self.discard_pile = []
            drawn_card = self.all_cards.pop()
            self.discard_pile.append("Attack")
            self.previous_card = drawn_card
            if  self.previous_card == "Skip" and self.previous_card == "Attack":
                print("You played a Skip card as a defense to an Attack card. It only ends 1 of the 2 turns.")
                self.previous_card = "Skip"
            else:
                self.discard_pile.append(self.previous_card)
                self.previous_card = "Attack"
            self.discard_pile.append(drawn_card)

    def skip_card_handler(self):
        '''
        Handles the case when the player draws a Skip card
        Helps players to skip their turns without drawing the card from the deck.
        '''
        self.discard_pile.append("Skip")
        print("You skipped your turn.")
    

    def favour_card_handler(self):
        '''
        Handles the case when the player draws a Favor card.
        Implements logic to request a card from other player.
        Once, player uses the action card, it is added to the discarded pile.
        '''
        player_choice = input("Which player would you like to choose to get a card from?:")
        for i in range(len(self.players)):
            if self.players[i].name == player_choice:
                if len(self.players[i].hand) == 0:
                    print(player_choice + " has no cards!")
                else:
                    requested_card = input(player_choice + ", choose a card to give:")
                    if requested_card in self.players[i].hand:
                        self.players[i].hand.remove(requested_card)
                        self.current_player.hand.append(requested_card)
                        print(player_choice + " gave you a " + requested_card + ".")
                    else:
                        print(player_choice + " doesn't have that card!")
                        random_card = random.choice(self.players[i].hand)
                        self.players[i].hand.remove(random_card)
                        self.current_player.hand.append(random_card)
                        print(player_choice + " gave you a " + random_card + " instead.")
            self.discard_pile.append("Favor")

    def nope_card_handler(self, drawn_card):
        '''
        Handles the case when the player draws a Nope card
        Parameter:
            drawn_card: str
                The card that was drawn from the deck.
        '''
        print("You played a Nope card!")
        # If the previous action was a 'Nope', negate it and create a 'Yup'
        if self.discard_pile and self.discard_pile[-1] == "Nope":
            self.discard_pile.pop()
            self.discard_pile.append("Yup")
        # Otherwise, stop any action except for an Exploding Kitten or a Defuse card
        else:
            noped_cards = [drawn_card]
            while True:
                print("Cards you noped: " + ", ".join(noped_cards))
                input_str = input(
                    "Do you want to still continue noping? Type 'yes' or 'no': "
                )
                if input_str.lower() != "yes":
                    break
                drawn_card = self.current_player.draw_card()
                if drawn_card in ["Exploding Kitten", "Defuse"]:
                    print("Sorry, You are not allowed to nope Defuse or Exploding Kitten  cards.")
                    self.discard_pile.append(drawn_card)
                    break
                else:
                    noped_cards.append(drawn_card)
            self.discard_pile.extend(noped_cards)
            self.shuffle_discard_pile()

    def shuffle_card_handler(self):
        '''
        Handles the case when the player draws a Shuffle card
        '''
        # Shuffle the remaining cards in the all_cards and add them to the discard pile as the new all_cards
        if self.discard_pile:
            new_all_cards = self.all_cards + self.discard_pile[:-1]
            random.shuffle(new_all_cards)
            self.discard_pile = [self.discard_pile[-1]] + new_all_cards
        else:
            new_all_cards = (self.all_cards) 
            # Exclude the most recent discard card, which is the 'shuffle' card itself
            random.shuffle(new_all_cards)
            self.discard_pile = new_all_cards
        self.discard_pile.append("Shuffle")
        print("You played a Shuffle card!  All cards has been shuffled and placed in the middle of the table.")

    def see_the_future_card_handler(self):
        '''
        Handles the case when the player draws a See The Future card
        '''
        print("You looked at the top three cards of the all_cards.")
        random.shuffle(self.all_cards)
        for i in range(3):
            if len(self.all_cards) == 0:
                print("The all_cards is empty!")
            else:
                print(self.all_cards[-1])
                self.all_cards.insert(0, self.all_cards.pop())

    def taco_card_handler(self, drawn_card):
        '''
        Handles the case when the player draws a Taco card
        Parameter:
            drawn_card: str
                The card that was drawn from the deck.
        '''
        print("You get to go again!")
        drawn_card = self.current_player.draw_card()
        if drawn_card is not None:
            print("You took out a " + drawn_card + ".")
            self.current_player.add_card(drawn_card)
        self.discard_pile.append("Taco Cat")

    def beardcat_handler(self):
        '''
        Handles the case when the player draws a Beard card.
        Player is allowed to steal random card from the other player.
        '''
        print("You can steal a random card from the other player!")
        other_player_index = (self.current_player_index + 1) % len(self.players)
        other_player = self.players[other_player_index]
        stolen_card = other_player.steal_card()
        if stolen_card is None:
            print("Sorry, The other player does not have card to steal!")
        else:
            self.current_player.add_card(stolen_card)
            print("You stole a " + stolen_card + " from the other player!")
        self.discard_pile.append("Beard Cat")

    def rainbow_ralphing_cat_handler(self):
        '''
        Handles the case when the player draws a Rainbow Ralphing Cat card
        Player needs to give a random card to the other player.
        '''
        print("You have to give a random card to the other player!") 
        other_player_index = (self.current_player_index + 1) % len(self.players)
        other_player = self.players[other_player_index]
        given_card = self.current_player.give_card()
        if given_card is None:
            print("You have no cards to give!")
        else:
            other_player.add_card(given_card)
            print("You gave a " + given_card + " to the other player!")
        self.discard_pile.append("Rainbow-Ralphing Cat")

    def favor_cat_handler(self):
        '''
        Handles the case where the player draws a pairing of favor Cat cards
        '''
        print("You need to ask the other player for a card of your choice!")
        other_player_index = (self.current_player_index + 1) % len(self.players)
        other_player = self.players[other_player_index]
        requested_card = input("Which card do you want to? ")
        received_card = other_player.give_specific_card(requested_card)
        if received_card is None:
            print(f"other player doesnot have a {received_card} to give you back!")
        else:
            self.current_player.add_card(received_card)
            print(f"You got a {received_card} from other player")
        self.discard_pile.append(received_card)

    def cat_cards_handler(self): 
        '''
        Handles the case where the player draws a pairing of Cat cards
        '''
        self.cat_cards = [card for card in self.current_player.hand if card.endswith("Cat")]
        if len(self.cat_cards) >= 2:
            self.cat_card_names = [card[:-4] for card in self.cat_cards]
            if self.cat_card_names[0] == self.cat_card_names[1]:
                print("You have a Pair of matching Cat Cards!")
                other_players = [p for p in self.players if p != self.current_player]
                if len(other_players) > 0:
                    chosen_player = random.choice(other_players)
                    stolen_card = chosen_player.give_card()
                    if stolen_card is not None:
                        self.current_player.hand.append(stolen_card)
                        print(f"You stole a {stolen_card} from {chosen_player.name}!")
                self.current_player.cat_cards.extend(self.cat_cards)
                self.current_player.hand = [card for card in self.current_player.hand if card not in self.cat_cards]
        else:
            print("You don't have a pair of matching Cat Cards.")
    

    def cattermelon_card_handler(self, drawn_card):
        '''
        Handles the case where the player draws a Cattermelon card
        Parameter:
            drawn_card: str
                The card that was drawn from the deck.
        '''
        print("You get to draw three additional cards!")
        for i in range(3):
            drawn_card = self.current_player.draw_card()
            if drawn_card is None:
                break
            print("You drew a " + drawn_card + ".")
        self.discard_pile.append("Cattermelon")
            

    
    def all_cards_handler(self, drawn_card):

        '''
        Handles the different types of cards in the Exploding Kittens game by calling the appropriate card handler function. This approach uses a dictionary to map cards to their 
        handler functions and using a common method to handle all the cards  making code reusable. So, it has the logic to handle each card type. 

        Parameters
        ----------
        drawn_card : str
            The card that was drawn from the deck.

        Returns
        -------
        None

        Raises
        ------
        None

        Notes
        -----
        The different types of cards and their corresponding handler functions are:
        - "Defuse": defuse_card_handler
        - "Attack": attack_card_handler
        - "Skip": skip_card_handler
        - "Favor": favour_card_handler
        - "Nope": nope_card_handler
        - "Shuffle": shuffle_card_handler
        - "See the Future": see_the_future_card_handler
        - "Taco Cat": taco_card_handler
        - "Beard Cat": beardcat_handler
        - "Rainbow Ralphing Cat": rainbow_ralphing_cat_handler
        - "Favor Cat": favor_cat_handler
        - "Cattermelon": cattermelon_card_handler

        If the drawn card is not one of the above types of cards, and is instead a cat card, the cat_cards_handler function is called. If the drawn card is not one of the above types of cards 
        and is not a cat card, it is added to the current player's hand.

        If the handler function for the drawn card requires an argument (i.e., the number of players for the Attack card), the handler function is called with the drawn_card argument. 
        Otherwise, the handler function is called with no arguments.
       
        '''
        handlers = {
            "Defuse": self.defuse_card_handler,
            "Attack": self.attack_card_handler,
            "Skip": self.skip_card_handler,
            "Favor": self.favour_card_handler,
            "Nope": self.nope_card_handler,
            "Shuffle": self.shuffle_card_handler,
            "See the Future": self.see_the_future_card_handler,
            "Taco Cat": self.taco_card_handler,
            "Beard Cat": self.beardcat_handler,
            "Rainbow Ralphing Cat": self.rainbow_ralphing_cat_handler,
            "Favor Cat": self.favor_cat_handler,
            "Cattermelon": self.cattermelon_card_handler
        }

        if drawn_card in handlers:
            handler = handlers[drawn_card]
            if handler.__code__.co_argcount > 1:
                handler(drawn_card)
            else:
                handler()
        elif drawn_card in self.cat_cards:
            self.cat_cards_handler()
        else:
            self.current_player.add_card(drawn_card)


    def play_game(self):

        """
        Method play_game:

        This method executes the main game loop where players take turns drawing and playing cards. It handles the logic for
        drawing cards, playing Exploding Kittens, handling special cards, checking if a player has won, and moving on to the
        next player.

        Inputs:
        - None

        Outputs:
        - None

        Raises
        ------
        IndexError
        If there are no players in the game.
  
        Process:
        1. Set the initial current player as the first player in the player list.
        2. Start the main game loop.
        3. Draw a card for the current player.
        4. If the drawn card is an Exploding Kitten, call the exploding_kitten__card_handler method to handle the event.
        5. If there is only one player left, they win.
        6. If the drawn card is in the current player's hand, remove it.
        7. If the drawn card is not an Exploding Kitten, call the all_cards_handler method to handle the event.
        8. Check if the current player has any cards left in their hand.
        9. If the current player has no cards left, they win.
        10. Move on to the next player.
        """

        drawn_card = None
        while True:
            self.current_player = self.players[self.current_player_index]
            print("*************************************************")
            print(f"{self.current_player.name}'s turn.")
            # if want to see cards on player's hands
            # print(f"{self.current_player.name} has these {self.current_player.hand}cards in his hands.")
            input("Press enter to draw a card.")
            drawn_card = self.current_player.draw_card()
            if drawn_card is None:
                break
            print("You drew a " + drawn_card + ".")
            if drawn_card == "Exploding Kitten":
                self.exploding_kitten__card_handler()
                if len(self.players) == 1:
                    print(self.players[0].name + " wins!")
                    break
                if drawn_card in self.current_player.hand:
                    self.current_player.hand.remove(drawn_card)
            else:
                self.all_cards_handler(drawn_card)

            # Check if the player has any cards left in their hand
            if len(self.current_player.hand) == 0:
                print(self.current_player.name + " has no cards left and wins the game!")
                break

            # Move on to the next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
  

            
           


             