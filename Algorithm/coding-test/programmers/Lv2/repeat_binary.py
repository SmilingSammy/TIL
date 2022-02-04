def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[0] += 1  # 이진 변환 횟수 update
        answer[1] += s.count('0')  # 0 제거 수 update
        length = s.count('1')  # 0 제거 후 길이
        s = bin(length)[2:]

    return answer