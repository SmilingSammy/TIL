def solution(n):
    decimals = [2]
    for num in range(3, n+1):
        decimals.append(num)
        sqrt_num = int(pow(num, 0.5)+1)
        for c in decimals:
            if c > sqrt_num:
                break
            if num % c == 0:
                decimals.pop()
                break
    return len(decimals)