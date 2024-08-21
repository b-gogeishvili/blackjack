from display import Card
from players import Player, Computer, Operations

from typing import Optional, Tuple


class Game:
    """ Handles all of game rules and functionality """
    def __init__(self, player: Player, computer: Computer) -> None:
        self._sides = {
            "computer": computer,
            "player": player, 
        }
        self.player = player
        self.computer = computer


    # TODO: catch blackjack (if score 21)
    def deal(self) -> Tuple[bool, Optional[Operations]]: 
        """ Initialize the game """
        blackjack = (False, None)
        for _, side in self._sides.items():
            side.cards += [
                Card.get_random_card() for _ in range(2)
            ]

            score = side.calculate_score() 
            if 21 in score and blackjack[0] == False:
                blackjack = (True, side)

        return blackjack

    def restart(self) -> None:
        """ Restart the game """
        for side in self._sides:
            self._sides[side].cards = []
        self.deal()
    
    def display_cards(self, is_blackjack : bool = False) -> None:
        """ Display cards of all participants (player and dealer) """
        for side in self._sides:
            op = self._sides[side]
            score = max(op.calculate_score())
            
            if op.name == "Player":
                print(f"{side.capitalize()}'s hand <Score: {score}>")
                self._sides[side].print_cards()
            else:
                print(f"{side.capitalize()}'s hand")
                self._sides[side].print_cards(is_blackjack)

            print()

