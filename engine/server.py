import sys

from game import Game
from players import Player, Computer
from cards import card_names


def card_code(card):
    return card_names[card.name] + card.suite_name[0]


game = None

for line in sys.stdin:
    command = line.strip()

    if command == "deal":
        game = Game(Player(name="test", cash=500), Computer())
        game.deal()

        player_cards = [card_code(c) for c in game.player.cards]
        dealer_cards = [card_code(c) for c in game.computer.cards]
        dealer_cards[-1] = "??"

        print("PLAYER", *player_cards)
        print("DEALER", *dealer_cards)
        print("STATUS playing")
        print("END")
    elif command == "quit":
        break
    else:
        print("ERROR unknown command")
        print("END")

