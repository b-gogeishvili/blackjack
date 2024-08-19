from game_ops import Game
from players import Player, Computer
from display import clear

game_is_running = True

while game_is_running:
    game = Game(Player(name="test", cash=500), Computer())

    print("BlackJack game!!!\n")
    game.display_cards()

    game_is_running = False
