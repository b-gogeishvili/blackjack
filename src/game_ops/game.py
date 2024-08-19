from display import Card
from players import Player, Computer


class Game:
    """ Handles all of game rules and functionality """
    def __init__(self, player: Player, computer: Computer) -> None:
        self._sides = {
            "computer": computer,
            "player": player, 
        }
        self.player = player
        self.computer = computer
        self.deal()


    # TODO: catch blackjack (if score 21)
    def deal(self) -> None:
        """ Initialize the game """
        for side in self._sides:
            self._sides[side].cards += [
                Card.get_random_card() for _ in range(2)
            ]

    def restart(self) -> None:
        """ Restart the game """
        for side in self._sides:
            # self._sides[side].reset_hand()
            self._sides[side].cards = []
        self.deal()
    
    def display_cards(self) -> None:
        """ Display cards of all participants (player and dealer) """
        for side in self._sides:
            print(f"{side}'s hand")
            self._sides[side].print_cards()
    
    # player_wins()
    # busted()
    # ...
