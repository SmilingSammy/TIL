def solution(s):
    x = list(s)
    return "".join(sorted(x, reverse=True))