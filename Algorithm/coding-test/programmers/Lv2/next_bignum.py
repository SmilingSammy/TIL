def solution(n):
    bin_n = bin(n)[2:]
    count1 = bin_n.count('1')

    for num in range(n + 1, 1000001):
        if count1 == bin(num)[2:].count('1'):
            return num

    return i