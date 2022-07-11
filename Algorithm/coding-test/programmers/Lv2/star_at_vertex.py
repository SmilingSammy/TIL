import math


def intersection(A, B, C, D, E, F):
    denom = A * D - B * C

    if denom == 0:
        return None, None

    x = (B * F - E * D) / denom
    y = (E * C - A * F) / denom

    if x == int(x) and y == int(y):
        return int(x), int(y)
    else:
        return None, None


def solution(line):
    points = set()
    inf = math.inf

    x_min, x_max, y_min, y_max = inf, -inf, inf, -inf
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, E, C, D, F = line[i] + line[j]
            x, y = intersection(A, B, C, D, E, F)

            if x == None:
                continue

            points.add((x, y))

            x_min = min(x, x_min)
            x_max = max(x, x_max)
            y_min = min(y, y_min)
            y_max = max(y, y_max)

    arr = [['.' for _ in range(x_max - x_min + 1)]
           for _ in range(y_max - y_min + 1)]

    for x, y in points:
        arr[y_max - y][x - x_min] = '*'

    return [''.join(elem) for elem in arr]