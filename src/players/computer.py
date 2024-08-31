from exceptions import ComputerBusted
from display import Card, utils
from . import Operations


class Computer(Operations):
    def __init__(self):
        super().__init__("Computer")
        self.name = "Computer"


    def evaluate(self) -> int:
        """ Add cards to the list if score is 16 or less """
        current_score = self.calculate_score()
        while (current_score < 17):  
            new_card = Card.get_random_card()
            self.cards.append(new_card)
            
            current_score = self.calculate_score()

            if self.is_busted():
                raise ComputerBusted()

        return current_score

    def print_cards(self, is_finished : bool = False) -> None:
        """ Print cards for the dealer. Last card is hidden """
        num_of_cards = len(self.cards)
        num_of_lines = len(utils.card.split("\n"))

        for line in range(num_of_lines):
            for i in range(num_of_cards):
                if i + 1 == num_of_cards and not is_finished:
                    card_visual_list = self.cards[i].visual(_hidden=True).split("\n")
                else:
                    card_visual_list = self.cards[i].visual().split("\n")

                print(card_visual_list[line], end=" ")
                
            print()

