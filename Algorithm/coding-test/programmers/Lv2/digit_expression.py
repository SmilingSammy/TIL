def solution(n):
    answer = 1  # 자기 자신 (ex. 15=15)

    for i in range(1, n // 2 + 1):
        tmp = i

        for j in range(i + 1, 10000):
            if tmp + j < n:
                tmp += j
                continue
            else:
                if tmp + j == n:
                    answer += 1
                break

    return answer


# def solution(n):
#     res = [i for i in range(1, n + 1, 2) if n % i == 0]
#
#     return len(res)