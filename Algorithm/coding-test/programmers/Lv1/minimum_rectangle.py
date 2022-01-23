def solution(sizes):
    max_r, max_c = 0, 0

    for size in sizes:
        r, c = sorted(size, reverse=True)
        max_r = max(r, max_r)
        max_c = max(c, max_c)

    return max_r * max_c