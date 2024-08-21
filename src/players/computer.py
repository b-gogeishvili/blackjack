from .ops import Operations
from display import Card, utils

class Computer(Operations):
    def __init__(self):
        super().__init__("Computer")
   

    # TODO: finish the loop to add cards, if applicable
        self.name = "Computer"
    def stand(self) -> list[int]:
        """ Add cards to the list if score is 16 or less """
        new_card = Card.get_random_card()
        self.cards.append(new_card)

        return self.calculate_score()

    def print_cards(self, is_blackjack : bool = False) -> None:
        """ Evaluate the winner. Last card is hidden """
        num_of_cards = len(self.cards)
        num_of_lines = len(utils.card.split("\n"))

        for line in range(num_of_lines):
            for i in range(num_of_cards):
                if i + 1 == num_of_cards and not is_blackjack:
                    card_visual_list = self.cards[i].visual(_hidden=True).split("\n")
                else:
                    card_visual_list = self.cards[i].visual().split("\n")

                print(card_visual_list[line], end=" ")
                
            print()
