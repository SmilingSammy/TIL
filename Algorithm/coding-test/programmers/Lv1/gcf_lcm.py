def solution(n, m):
    multi_val = n * m
    while n != 0:
        m, n = n, m % n

    return [m, int(multi_val / m)]