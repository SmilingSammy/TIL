def convert(n, k):
    q, r = divmod(n, k)

    return convert(q, k) + str(r) if q else str(r)


def decimal(num):
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False

    return True


def solution(n, k):
    x = convert(n, k)
    candidates = x.split('0')
    answer = 0

    for c in candidates:
        if c == '1' or c == '':
            continue

        if decimal(int(c)):
            answer += 1

    return answer