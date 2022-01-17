def solution(n):
    if n == 0:
        return 0

    answer = []
    for i in range(1, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            answer.append(i)
            answer.append(n // i)

    return sum(list(set(answer)))