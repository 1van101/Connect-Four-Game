from four_connection_game.utils.check_for_winner import player_wins
from four_connection_game.utils.placing_turn import player_turn, matrix_is_full
from four_connection_game.utils.start_the_game import starting_game, play_again
from four_connection_game.utils.exceptions import FullColumnError, InvalidIndexError
from colorama import Fore, Style


def play():
    ROWS, COLS = 6, 7
    WINNING_NUM = 4
    first_player = input("Please enter a sign for the first player: ").upper()
    second_player = input("Please enter a sign for the second player: ").upper()

    board, turns = starting_game(ROWS, COLS)

    while True:

        game_over = False
        turns += 1
        current_player_sign = second_player if turns % 2 == 0 else first_player

        try:
            player_choice_col = int(input(f"\n{Style.RESET_ALL}PLayer {current_player_sign},"
                                          f" please enter a number of column in range (1 - {COLS}): ")) - 1

            player_row, player_col = \
                player_turn(board, player_choice_col, current_player_sign, first_player, second_player)

            if player_wins(board, player_row, player_col, current_player_sign, WINNING_NUM):
                print(Fore.GREEN + f"The winner is PLAYER {current_player_sign}" + Fore.RESET + "\n")
                game_over = True

            if matrix_is_full(board):
                print(Fore.RED + "The board is full, the game is over, nobody wins!" + Fore.RESET)
                game_over = True

        except FullColumnError:
            print(Fore.RED + "This column is full. Please try with another column next time!" + Fore.RESET)
        except InvalidIndexError:
            print(Fore.RED + "Please enter valid column next time!" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Your choice must be an integer in given range only!" + Fore.RESET)

        if game_over:
            if play_again():
                board, turns = starting_game(ROWS, COLS)
            else:
                print("Hope to see you soon")
                break


if __name__ == "__main__":
    play()
