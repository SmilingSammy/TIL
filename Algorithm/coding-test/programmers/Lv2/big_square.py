def solution(board):
    result = set()

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                result.add(board[i][j])

    maximum = max(result) if result else max(sum(board, []))

    return pow(maximum, 2)