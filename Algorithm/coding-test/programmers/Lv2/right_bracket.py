def solution(s):
    count = 0

    for brk in s:
        if brk == '(': count += 1
        else: count -= 1

        if count < 0: return False

    return True if count == 0 else False