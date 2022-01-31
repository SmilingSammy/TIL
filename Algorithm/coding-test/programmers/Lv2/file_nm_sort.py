import re


def solution(files):
    f1 = lambda x: re.findall('[^0-9]+', x)[0].lower()
    f2 = lambda x: int(re.findall('[0-9]+', x)[0])

    return sorted(files, key=lambda x: (f1(x), f2(x)))