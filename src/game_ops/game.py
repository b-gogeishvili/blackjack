from display import Card
from players import Player, Computer


class Game:
    """ Handles all of game rules and functionality """
    def __init__(self, player: Player, computer: Computer) -> None:
<<<<<<< HEAD
        self._sides = {
            "computer": computer,
            "player": player, 
=======
        self.sides = {
            "player": player,
            "computer": computer
>>>>>>> 2a7e95bb2e674d2e65b322b078fe160a9b4913cf
        }
        self.player = player
        self.computer = computer
        self.deal()


    # TODO: catch blackjack (if score 21)
    def deal(self) -> None:
        """ Initialize the game """
        for side in self._sides:
            self._sides[side].cards += [
                Card.get_random_card() for _ in range(2)
            ]

    def restart(self) -> None:
<<<<<<< HEAD
        """ Restart the game """
        for side in self._sides:
            self._sides[side].cards = []
        self.deal()
    
    def display_cards(self) -> None:
        """ Display cards of all participants (player and dealer) """
        for side in self._sides:
            print(f"{side}'s hand")
            self._sides[side].print_cards()
=======
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
>>>>>>> 2a7e95bb2e674d2e65b322b078fe160a9b4913cf

    # player_wins()
    # busted()
    # ...
