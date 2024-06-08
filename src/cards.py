class Card:
    def __init__(self, name, suite, hidden=False) -> None:
        self.name = name
        self.symbol = card_names[name]
        self.suite_name = suite
        self.suite = suites[suite]
        self.hidden = hidden
        self.score = card_scores[self.symbol]

    def get_card_visual(self) -> str:
        if self.hidden:
            return hidden_card
        else:
            return card.format(self.symbol, self.suite, self.suite, self.suite, self.symbol)

    @property
    def get_score(self) -> int:
        return self.score
