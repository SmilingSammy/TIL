import string

def solution(s, n):
    lower_ls = list(string.ascii_lowercase * 3)
    upper_ls = list(string.ascii_uppercase * 3)

    answer = ""
    for elem in list(s):
        if elem.isalpha():
            if elem.islower():
                elem = lower_ls[lower_ls.index(elem) + n]
            else:
                elem = upper_ls[upper_ls.index(elem) + n]

        answer += elem

    return answer