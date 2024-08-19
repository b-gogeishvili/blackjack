from display import Card, utils

<<<<<<< HEAD
class Operations: 
    """ This class defines operations necessary for both player and dealer(computer) """
    def __init__(self) -> None:
        self.cards = []
    
    
=======
class Operations:
    def __init__(self) -> None:
        self.cards = []


    # Returns list because 'Ace' can have two values
>>>>>>> 2a7e95bb2e674d2e65b322b078fe160a9b4913cf
    def calculate_score(self) -> list[int]:
        """ Calculates overall score and returns list because 'Ace' can have two values """
        score = [0, 0]

        for card in self.cards:
            if card.name == "Ace":
                score[0] += card.score[0]
                score[1] += card.score[1]

                continue

            score[0] += card.score
            score[1] += card.score

        return score

    def hit(self) -> list[int]:
        """ Add another card to the list """
        new_card = Card.get_random_card()
        self.cards.append(new_card)
<<<<<<< HEAD

        return self.calculate_score()
    
    def stand(self) -> list[int]:
        """ Evaluate the winner """
        return self.calculate_score()
    
    def print_cards(self) -> None:
        """ Evaluate the winner """
        num_of_cards = len(self.cards)
        num_of_lines = len(utils.card.split("\n"))

        for line in range(num_of_lines):
            for i in range(num_of_cards):
                card_visual_list = self.cards[i].visual().split("\n")
                print(card_visual_list[line], end=" ")
                
            print()
=======
        # display_cards()

        return self.calculate_score()
>>>>>>> 2a7e95bb2e674d2e65b322b078fe160a9b4913cf

    def stand(self) -> list[int]:
        return self.calculate_score()

    def reset_hand(self) -> None:
        self.cards = []
