def convert(num, n):
    """ 진법 변환 """

    strs = ''.join(map(str, range(10))) + 'ABCDEF'
    q, r = divmod(num, n)

    return strs[r] if q == 0 else convert(q, n) + strs[r]


def solution(n, t, m, p):
    result = ''
    for num in range(t * m):
        result += convert(num, n)

    answer = ''
    for order in range(p - 1, t * m, m):
        answer += result[order]

    return answer