from four_connection_game.utils.exceptions import FullColumnError, InvalidIndexError
from colorama import Fore


def player_choice_is_valid(matrix, col):
    matrix_cols = len(matrix[0])
    return col in range(matrix_cols)


def matrix_is_full(matrix):
    matrix_cols = len(matrix[0])
    return all([matrix[0][x] != "0" for x in range(matrix_cols)])


def color_pl_turn(matrix, pl1, pl2):
    print()
    for row in matrix:
        for cell in row:
            if cell == pl1:
                cell = Fore.BLUE + cell + Fore.RESET
            elif cell == pl2:
                cell = Fore.YELLOW + cell + Fore.RESET
            print(cell, end=" ")
        print()
    print()


def player_turn(matrix, col, curr_pl_sign, pl1, pl2):
    if player_choice_is_valid(matrix, col):
        for r in range(len(matrix) - 1, -1, -1):
            if matrix[r][col] == '0':
                matrix[r][col] = curr_pl_sign
                color_pl_turn(matrix, pl1, pl2)
                return r, col
        else:
            raise FullColumnError
    raise InvalidIndexError
