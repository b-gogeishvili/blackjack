from .utils import *
import random


class Card:
    """ Card related properties and methods """
    def __init__(self, name: str, suite: str) -> None:
        self.name = name
        self._symbol = card_names[name]
        self.suite_name = suite
        self._suite = suites[suite]
        self._score = card_scores[self._symbol]
   
 
    def visual(self, _hidden: bool = False) -> str:
        """ Visual representation of each card. Handles back of the card as hidden """
        if _hidden:
            return hidden_card
        elif self.name != "10":
            return card.format(self._symbol, self._suite, self._suite, self._suite, self._symbol)
        else:
            return exception.format(self._symbol, self._suite, self._suite, self._suite, self._symbol)

    @property
    def score(self) -> int:
        """ Returns score of the specific card """
        return self._score
    
    @staticmethod
    def get_random_card() -> 'Card':
        """ Returns randomly generated card """
        return Card (
            random.choice(list(card_names)),
            random.choice(list(suites))
        )

