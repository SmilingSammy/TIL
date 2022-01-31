def solution(land):
    for r in range(1, len(land)):
        for c in range(4):
            land[r][c] += max(land[r - 1][:c] + land[r - 1][c + 1:])

    return max(land[-1])