import math
def solution(n):
    val = pow(n, 0.5)
    return int(pow(val+1, 2)) if val == int(val) else -1