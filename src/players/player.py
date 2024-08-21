from . import Operations 

class Player(Operations):
    def __init__(self, name, cash) -> None:
        super().__init__("Player")
        self.username = name
        self.cash = cash


    def stand(self, computer : "Computer") -> list[int]:
        """
        Evaluate the winner. 
        Takes 'Computer' as an input and 
        returns list in the format -> [computer_score, player_score] 
        """
        return [computer.evaluate(), self.calculate_score()]
