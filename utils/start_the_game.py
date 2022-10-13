from colorama import Fore


def starting_game(R, C):
    matrix = [['0' for y in range(C)] for x in range(R)]
    turns = 0
    print()
    [print(' '.join(matrix[x])) for x in range(R)]
    return matrix, turns


def play_again():
    pl_choice = input("Do you want to play again?[Y/N]: ").lower()

    while True:
        if pl_choice == "y" or pl_choice == "n":
            return True if pl_choice == "y" else False
        else:
            print(Fore.RED + "The command should be only [Y/N]! Try again!\n" + Fore.RESET)
        pl_choice = input().lower()
