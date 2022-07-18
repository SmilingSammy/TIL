from copy import deepcopy


def remove(new_board):
    # copy
    tmp_board = deepcopy(new_board)

    # row, col length
    m = len(tmp_board)
    n = len(tmp_board[0])

    for i in range(m - 1):
        for j in range(n - 1):
            block = new_board[i][j]
            check_same = all(
                map(lambda x: block == x, (new_board[i][j + 1], new_board[i + 1][j], new_board[i + 1][j + 1])))

            if check_same:
                for r, c in ([i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]):
                    tmp_board[r][c] = ''

    return tmp_board


def drop(tmp_board):
    tmp_board = list(zip(*tmp_board))

    for i in range(len(tmp_board)):
        tb = tmp_board[i]
        remove_count = tb.count('')
        tmp_board[i] = [''] * remove_count + list(filter(lambda x: x != '', tb))

    tmp_board = list(map(list, zip(*tmp_board)))

    return tmp_board


def solution(m, n, board):
    new_board = []
    for b in board:
        new_board.append(list(b))

    tmp_board = remove(new_board)
    tmp_board = drop(tmp_board)

    while new_board != tmp_board:
        new_board = tmp_board
        tmp_board = remove(new_board)
        tmp_board = drop(tmp_board)

    return sum(new_board, []).count('')