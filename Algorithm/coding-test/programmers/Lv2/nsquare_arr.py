def solution(n, left, right):
    answer = []

    for x in range(left, right + 1):
        r, c = divmod(x, n)
        answer.append(max(r + 1, c + 1))

    return answer