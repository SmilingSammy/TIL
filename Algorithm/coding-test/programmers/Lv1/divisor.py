def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        count = 0

        x_sqrt = pow(x, 0.5)
        if x_sqrt == int(x_sqrt):
            count += 1

        for i in range(1, int(x_sqrt)):
            if x % i == 0:
                count += 2

        if count % 2 == 0:
            answer += x
        else:
            answer -= x

    return answer