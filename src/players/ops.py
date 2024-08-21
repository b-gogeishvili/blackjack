from display import Card, utils

class Operations: 
    """ 
    This class defines operations necessary for both - 
    player and dealer(computer)
    """
    def __init__(self, name) -> None:
        self.cards = []
        self.name = name
    

    def calculate_score(self) -> int:
        """ 
        Calculates score and returns it according to the 'Ace' value.
        'Ace' can have score 1 or 11. If we take 'Ace' as 11
        and score exceeds 21, we will use 'Ace' as 1 instead.
        """
        score = [0, 0]

        for card in self.cards:
            if card.name == "Ace":
                score[0] += card.score[0]
                score[1] += card.score[1]

                continue

            score[0] += card.score
            score[1] += card.score

        return max(score) if max(score) < 21 else min(score)
 
    def hit(self) -> int:
        """ Add another card to the list and returns score """
        new_card = Card.get_random_card()
        self.cards.append(new_card)

        if self.is_busted():
            return -1

        return self.calculate_score()
    
    def stand(self, computer : "Computer") -> list[int]:
        """
        Evaluate the winner. 
        Takes 'Computer' as an input and 
        returns list in the format -> [computer_score, player_score] 
        """
        if computer.stand()[0] == -1:
            return [-1]

        return [self.calculate_score()]
    
    def print_cards(self) -> None:
        """ Print cards on the screen """
        num_of_cards = len(self.cards)
        num_of_lines = len(utils.card.split("\n"))

        for line in range(num_of_lines):
            for i in range(num_of_cards):
                card_visual_list = self.cards[i].visual().split("\n")
                print(card_visual_list[line], end=" ")
                
            print()

    def is_busted(self) -> bool:
        """ Check if score exceeded 21 """
        if self.calculate_score() > 21:
            return True
        else:
            return False

