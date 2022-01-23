from itertools import combinations

def solution(numbers):
    candidates = list(combinations(numbers, 2))
    return sorted({sum(c) for c in candidates})