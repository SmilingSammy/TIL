def solution(a, b):
    answer = 0

    for val in range(min(a, b), max(a, b) + 1):
        answer += val

    return answer