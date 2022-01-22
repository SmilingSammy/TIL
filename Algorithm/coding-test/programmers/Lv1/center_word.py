def solution(s):
    if len(s) % 2 != 0 :
        return s[int(len(s) / 2)]
    else:
        idx = len(s) // 2 -1
        return s[idx:idx+2]