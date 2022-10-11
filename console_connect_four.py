from colorama import Fore, Style


class FullColumnError(Exception):
    pass


class InvalidIndexError(Exception):
    pass


class MinimumInputValue(Exception):
    pass


def player_choice_is_valid(C, checked_idx):
    return checked_idx in range(C)


def starting_game(r, c):
    matrix = [['0' for y in range(c)] for x in range(r)]
    turns = 0
    [print(' '.join(matrix[x])) for x in range(r)]
    return matrix, turns


def matrix_is_full(matrix, c):
    return all([matrix[0][x] != "0" for x in range(c)])


def color_the_choice(matrix, player1, player2):
    for row in matrix:
        for cell in row:
            if cell == player1:
                cell = Fore.BLUE + cell + Fore.RESET
            elif cell == player2:
                cell = Fore.YELLOW + cell + Fore.RESET
            print(cell, end=" ")
        print()


def player_turn(matrix, c, matrix_cols, player_sign, player1, player2):
    if player_choice_is_valid(matrix_cols, c):
        for r in range(len(matrix) - 1, -1, -1):
            if matrix[r][c] == '0':
                matrix[r][c] = player_sign
                color_the_choice(matrix, player1, player2)
                return r, c
        else:
            raise FullColumnError
    raise InvalidIndexError


def check_cell(matrix, r, c, player):
    if c < 0 or r < 0:
        return False
    try:
        if matrix[r][c] == player:
            return True
    except IndexError:
        return False
    return False


def check_vertical(matrix, r, c, player, winning_num):
    try:
        return all([True if matrix[r + x][c] == player else False for x in range(winning_num)])
    except IndexError:
        return False


def check_horizontal(matrix, r, c, player, winning_num):
    matches = set()

    for i in range(winning_num):
        if check_cell(matrix, r, c + i, player):
            matches.add((r, c + i))
        else:
            break

    for i in range(winning_num):
        if check_cell(matrix, r, c - i, player):
            matches.add((r, c - i))
        else:
            break
    return len(matches) >= winning_num


def descending_diagonal(matrix, r, c, player, winning_num):
    matches = set()

    for i in range(winning_num):
        if check_cell(matrix, r - i, c - i, player):
            matches.add((r - i, c - i))
        else:
            break

    for i in range(winning_num):
        if check_cell(matrix, r + i, c + i, player):
            matches.add((r + i, c + i))
        else:
            break

    return len(matches) >= winning_num


def ascending_diagonal(matrix, r, c, player, winning_num):
    matches = set()

    for i in range(winning_num):
        if check_cell(matrix, r - i, c + i, player):
            matches.add((r - i, c + i))
        else:
            break

    for i in range(winning_num):
        if check_cell(matrix, r + i, c - i, player):
            matches.add((r + i, c - i))
        else:
            break

    return len(matches) >= winning_num


def player_wins(matrix, r, c, player, winning_num):
    return any([
        check_vertical(matrix, r, c, player, winning_num),
        check_horizontal(matrix, r, c, player, winning_num),
        ascending_diagonal(matrix, r, c, player, winning_num),
        descending_diagonal(matrix, r, c, player, winning_num)
    ])


def want_to_play_again():
    player_choice = input("Do you want to play again?[Y/N]").lower()

    while True:
        if player_choice == "y" or player_choice == "n":
            return True if player_choice == "y" else False
        else:
            print(Fore.RED + "The command should be only [Y/N]! Try again!" + Fore.RESET)
        player_choice = input().lower()


def play():
    ROWS, COLS = 6, 7
    WINNING_NUM = 4
    first_player, second_player = '1', '2'

    board, turns = starting_game(ROWS, COLS)

    while True:

        game_over = False
        turns += 1
        current_player_sign = second_player if turns % 2 == 0 else first_player

        try:
            player_choice_col = int(input(f"\n{Style.RESET_ALL}PLayer {current_player_sign},"
                                          f" please enter a number of column in range (1 - {COLS}): "))

            player_row, player_col = \
                player_turn(board, player_choice_col - 1, COLS, current_player_sign, first_player, second_player)

            if player_wins(board, player_row, player_col, current_player_sign, WINNING_NUM):
                print(Fore.GREEN + f"The winner is PLAYER {current_player_sign}" + Fore.RESET)
                game_over = True

            if matrix_is_full(board, COLS):
                print(Fore.RED + "The board is full, the game is over, nobody wins!" + Fore.RESET)
                game_over = True

        except FullColumnError:
            print(Fore.RED + "This column is full. Please try with another column next time!" + Fore.RESET)
        except InvalidIndexError:
            print(Fore.RED + "Please enter valid column next time!" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Your choice must be an integer in given range only!" + Fore.RESET)

        if game_over:
            if want_to_play_again():
                board, turns = starting_game(ROWS, COLS)
            else:
                print("Hope to see you soon")
                break


if __name__ == "__main__":
    play()
