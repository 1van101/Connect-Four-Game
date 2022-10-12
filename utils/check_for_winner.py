def cell_matches(matrix, row, col, pl_sign):
    if col < 0 or row < 0:
        return False
    try:
        if matrix[row][col] == pl_sign:
            return True
    except IndexError:
        return False
    return False


def vertical(matrix, row, col, pl_sign, win_num):
    try:
        return all([True if matrix[row + i][col] == pl_sign else False for i in range(win_num)])
    except IndexError:
        return False


def horizontal(matrix, row, col, pl_sign, win_num):
    matches = set()

    for i in range(win_num):
        if cell_matches(matrix, row, col + i, pl_sign):
            matches.add((row, col + i))
        else:
            break

    for i in range(win_num):
        if cell_matches(matrix, row, col - i, pl_sign):
            matches.add((row, col - i))
        else:
            break
    return len(matches) >= win_num


def descending_diagonal(matrix, row, col, pl_sign, win_num):
    matches = set()

    for i in range(win_num):
        if cell_matches(matrix, row - i, col - i, pl_sign):
            matches.add((row - i, col - i))
        else:
            break

    for i in range(win_num):
        if cell_matches(matrix, row + i, col + i, pl_sign):
            matches.add((row + i, col + i))
        else:
            break

    return len(matches) >= win_num


def ascending_diagonal(matrix, row, col, pl_sign, win_num):
    matches = set()

    for i in range(win_num):
        if cell_matches(matrix, row - i, col + i, pl_sign):
            matches.add((row - i, col + i))
        else:
            break

    for i in range(win_num):
        if cell_matches(matrix, row + i, col - i, pl_sign):
            matches.add((row + i, col - i))
        else:
            break

    return len(matches) >= win_num


def player_wins(matrix, row, col, pl_sign, win_num):
    return any([
        vertical(matrix, row, col, pl_sign, win_num),
        horizontal(matrix, row, col, pl_sign, win_num),
        ascending_diagonal(matrix, row, col, pl_sign, win_num),
        descending_diagonal(matrix, row, col, pl_sign, win_num)
    ])