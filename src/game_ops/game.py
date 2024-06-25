from display import Card, card_names, suites
from players import Player, Computer

import random

class Game:
    def __init__(self, player: Player, computer: Computer) -> None:
        self.sides = {
            "player": player,
            "computer": computer
        }
        self.deal()


    def deal(self) -> None:
        for side in self.sides:
            self.sides[side].cards += [
                get_random_card() for i in range(2)
            ]

    def restart(self) -> None:
        for side in self.sides:
            self.sides[side].reset_hand()
        self.deal()

    def display_cards(self) -> None:
        # <---- Computer ---->
        computer = self.sides["computer"]

        print("Computer's hand: ")

        to_display = [
            computer.cards[0].visual().split("\n"),
            computer.cards[1].visual(_hidden=True).split("\n")
        ]

        for i in range(len(to_display[0])):
            print(to_display[0][i] + "    " + to_display[1][i])



        # print(computer.cards[0].visual(), end="     ")
        # print(computer.cards[1].visual(_hidden = True), "\n\n")

        # <---- PLAYER ---->
        player = self.sides["player"]

        print(f"Player's hand: {player.calculate_score()}")
        for card in player.cards:
            print(card.visual(), end="     ")
        print("\n")


def get_random_card() -> Card:
    return Card (
        random.choice(list(card_names)),
        random.choice(list(suites))
    )

    # player_wins()
    # busted()
    # display_cards()
    # ...
