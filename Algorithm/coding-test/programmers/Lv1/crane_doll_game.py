def solution(board, moves):
    size = len(board)
    basket = []  # 인형 바구니
    count = 0  # 사라진 인형 수

    for m in moves:
        m -= 1  # 배열 index 접근을 위해 -1

        for s in range(size):
            if board[s][m] == 0:
                continue
            basket.append(board[s][m])
            board[s][m] = 0
            break

        if len(basket) > 1 and basket[-2] == basket[-1]:
            basket = basket[:-2]
            count += 2

    return count


# def solution(board, moves):
#     # 인형 뽑은 리스트
#     doll_ls = []
#     # 없앤 인형 Count
#     doll_disapper_count = 0
#
#     for move in moves:
#
#         for row in range(len(board)):
#             doll_num = board[row][move - 1]
#
#             if doll_num != 0:
#                 board[row][move - 1] = 0
#                 if len(doll_ls) > 0 and doll_ls[-1] == doll_num:
#                     doll_ls.pop()
#                     doll_disapper_count += 2
#
#                 else:
#                     doll_ls.append(doll_num)
#
#                 break
#
#     return doll_disapper_count