from game_ops import Game
from players import Player, Computer
from display import clear

game_is_running = True

def ask_for_continuation():
    if input("Do you want to continue? (y/n): ").lower() == "n":
        return False
    else:
        return True

# TODO 1: Make the game playable
# TODO 2: Add other methods if applicable
# TODO 3: Review if tests/error handling can be added
while game_is_running:
    game = Game(Player(name="test", cash=500), Computer())
    
    clear()
    print("Welcome to BlackJack game! \n")
    input("Press enter to continue: ")
    print()

    init_score = game.deal()
    current_score = init_score
    game.display_cards()
    
    if init_score[0] == True and init_score[1] is not None:
        clear()
        game.display_cards(is_blackjack = True)
        print(f"{init_score[1].name} got BlackJack!!!")
        
        if not ask_for_continuation():
            game_is_running = False

    if input("Press 'h' to Hit or 's' to Stand. (h/s): ").lower() == "h":
        game.player.hit()
