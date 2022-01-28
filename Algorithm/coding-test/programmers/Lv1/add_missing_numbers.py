def solution(numbers):
    total = {x for x in range(10)}
    nums = set(numbers)

    return sum(total - nums)