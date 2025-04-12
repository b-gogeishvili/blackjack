from game import Game
from players import Player, Computer
from cards import clear
from exceptions import PlayerBusted, ComputerBusted

import time

def help() -> None:
    pass

def header(first_time : bool = False) -> None: 
    clear()
    print("---- BlackJack game! ----\n")
    
    if first_time:
        print("Press enter to continue.")
        print("Type 'h' for game rules.")
        print("Type 'q' to quit.")

        help_char = input("\n---> ")
        print([help_char])

        if help_char.lower() == 'h':
            help()

    print()

def main() -> None:
    game_is_running = True
    game = Game(Player(name="test", cash=500), Computer())
    
    init_score = game.deal()

    while game_is_running:
        header()
        game.display_cards()

        # if init_score[0] == True and init_score[1] is not None:
        if init_score[1] is not None:
            clear()
            game.display_cards(is_finished = True)
            print(f"---- {init_score[1].name} got BlackJack!!!\n")
            break

        action = input("Press 'h' to Hit or 's' to Stand. (h/s): ").lower() 
        
        if action == "h":
            try:
                game.player.hit()
            except PlayerBusted as busted:
                clear()
                header()
                game.display_cards(is_finished = True)
                print(busted)
                break

            clear()
            game.display_cards()

        elif action == 's':
            try:
                computer_score, player_score = game.player.stand(game.computer)
            except ComputerBusted as busted:
                clear()
                header()
                game.display_cards(is_finished = True)
                print(busted)
                break

            clear()
            header()
            game.display_cards(is_finished = True)
            game_is_running = False

            if computer_score == player_score:
                print("---- Its a tie!\n")
            elif computer_score > player_score:
                print("---- Computer Won!\n")
            elif player_score > computer_score:
                print("---- Player Won!\n")
            else:
                raise Exception("Unexpected Error")
            
        else:
            raise Exception("Invalid Action")

if __name__ == "__main__":
    header(first_time = True)
    while True:
        clear()
        try:
            main()
        except Exception:
            print("\nSorry, something went wrong\n")

        if input("Do you want to play again? (y/n): ").lower() == "n":
            break

