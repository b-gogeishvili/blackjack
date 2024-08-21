from game_ops import Game
from players import Player, Computer
from display import clear

game_is_running = True

while game_is_running:
    game = Game(Player(name="test", cash=500), Computer())
    
    clear()
    print("Welcome to BlackJack game! \n")
    input("Press enter to continue: ")
    init_score = game.deal()
    
    game.display_cards()
    
    if init_score[0] == True and init_score[1] is not None:
        clear()
        game.display_cards(is_blackjack = True)
        print(f"{init_score[1].name} got BlackJack!!!")
        break

    clear()
    game.display_cards()

    if input("Do you want to continue? (y/n): ").lower() == "n":
        game_is_running = False
