def solution(n):
    # 현재 state
    state = 0

    while n != 0:
        n, step = divmod(n, 2)
        state += step

    return state