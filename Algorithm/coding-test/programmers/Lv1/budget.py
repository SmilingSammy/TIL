def solution(d, budget):
    answer = 0
    d.sort()

    for elem in d:
        if budget >= elem:
            budget -= elem
            answer += 1
        else:
            break

    return answer