def solution(n):
    count = 0
    while (n != 1) and (count < 500):
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1

    return -1 if count == 500 else count