from game_ops import Game
from players import Player, Computer
from display import clear

game_is_running = True

<<<<<<< HEAD
while game_is_running:
    game = Game(Player(name="test", cash=500), Computer())

    print("BlackJack game!!!\n")
=======
    game.restart()
>>>>>>> 2a7e95bb2e674d2e65b322b078fe160a9b4913cf
    game.display_cards()

    game_is_running = False
