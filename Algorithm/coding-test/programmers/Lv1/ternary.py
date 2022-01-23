def solution(n):
    def base3(num):
        q, r = divmod(num, 3)
        return base3(q) + str(r) if q else str(r)

    return int(base3(n)[::-1], 3)