from display import Card
from exceptions import PlayerBusted
from . import Operations 

class Player(Operations):
    def __init__(self, name, cash) -> None:
        super().__init__("Player")
        self.username = name
        self.cash = cash
   
    def hit(self) -> int:
        """ Add another card to the list and returns score """
        new_card = Card.get_random_card()
        self.cards.append(new_card)

        if self.is_busted():
            raise PlayerBusted()

        return self.calculate_score()

    def stand(self, computer : "Computer") -> list[int]:
        """
        Evaluate the winner. 
        Takes 'Computer' as an input and 
        returns list in the format -> [computer_score, player_score] 
        """
        return [computer.evaluate(), self.calculate_score()]
