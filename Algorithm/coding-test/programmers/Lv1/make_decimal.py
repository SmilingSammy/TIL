from itertools import combinations


def solution(nums):
    candidates = list(combinations(nums, 3))
    count = 0

    for c in candidates:
        c = sum(c)
        count +=1 
        for i in range(2, int(pow(c, 0.5) + 1)):
            if c % i == 0:
                count -= 1
                break

    return count