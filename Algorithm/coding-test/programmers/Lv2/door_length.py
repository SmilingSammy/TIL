def solution(dirs):
    direction = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}  # 방향
    x, y = 0, 0  # 초기화
    result = set()

    for d in dirs:
        cmd = direction[d]
        new_x, new_y = x + cmd[0], y + cmd[1]

        if new_x > 5 or new_y > 5 or new_x < -5 or new_y < -5:
            continue

        result.add((x, y, new_x, new_y))
        result.add((new_x, new_y, x, y))

        x, y = new_x, new_y

    return len(result) // 2