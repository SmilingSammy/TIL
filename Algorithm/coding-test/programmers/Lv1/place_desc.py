def solution(n):
    sort_str = sorted(str(n), reverse=True)
    return int("".join(sort_str))