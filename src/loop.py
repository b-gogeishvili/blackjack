from game_ops import Game
from players import Player, Computer
from display import Card
import random

def main():
    game = Game(Player(), Computer())

    game.display_cards()

main()
