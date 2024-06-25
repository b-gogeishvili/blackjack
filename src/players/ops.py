from display import Card, card_names, suites

class Operations:
    def __init__(self) -> None:
        self.cards = []


    # Returns list because 'Ace' can have two values
    def calculate_score(self) -> list[int]:
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
        from game_ops import get_random_card

        new_card = get_random_card()
        self.cards.append(new_card)
        # display_cards()

        return self.calculate_score()

    def stand(self) -> list[int]:
        return self.calculate_score()

    def reset_hand(self) -> None:
        self.cards = []
