def solution(arr):
    elem_arr = list(str(arr))
    sum_all = sum(list(map(int, elem_arr)))

    return True if arr % sum_all == 0 else False