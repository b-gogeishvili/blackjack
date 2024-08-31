from game_ops import Game
from players import Player, Computer
from display import clear
from exceptions import PlayerBusted, ComputerBusted

# TODO 1: Make the game playable
# TODO 2: Add other methods if applicable
# TODO 3: Review if tests/error handling can be added

def help() -> None:
    pass

def greeting() -> None: 
    clear()
    print("Welcome to BlackJack game! \n")
    help_char = input("Press enter to continue or type 'h' for game rules: ")

    if help_char.lower() == 'h':
        help()
    print()   

def main() -> None:
    game_is_running = True
    game = Game(Player(name="test", cash=500), Computer())
    

    while game_is_running:
        init_score = game.deal()
        game.display_cards()
        
        if init_score[0] == True and init_score[1] is not None:
            clear()
            game.display_cards(is_finished = True)
            print(f"{init_score[1].name} got BlackJack!!!")
            break

        action = input("Press 'h' to Hit or 's' to Stand. (h/s): ").lower() 
        
        if action == "h":
            try:
                game.player.hit()
            except PlayerBusted as busted:
                clear()
                game.display_cards(is_finished = True)
                print(busted)
                break

        elif action == 's':
            try:
                computer_score, player_score = game.player.stand(game.computer)
            except ComputerBusted as busted:
                clear()
                game.display_cards(is_finished = True)
                print(busted)
                break

            if computer_score == player_score:
                print("Its a tie!")
            elif computer_score > player_score:
                print("Computer Won!")
            elif player_score > computer_score:
                print("Player Won!")
            else:
                raise Exception("Unexpected Error")

            game_is_running = False

        else:
            raise Exception("Invalid Action")

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception:
            print("Sorry, something went wrong")

        if input("Do you want to play again? (y/n): ").lower() == "n":
            break
