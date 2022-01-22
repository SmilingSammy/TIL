def solution(s):
    if (len(s) != 4 and len(s) != 6):
        return False

    return True if s.isnumeric() else False