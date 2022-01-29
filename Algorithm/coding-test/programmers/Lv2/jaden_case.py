def solution(s):
    s = s.lower()
    answer = ''
    count = 0

    for text in s:
        if text == " ":
            answer += text
            count = 0
            continue

        answer += text if count != 0 else text.upper()
        count += 1

    return answer


# def solution(s):
#     s = s.lower()
#     answer = ''
#     count = 0
#
#     for text in s:
#         if text == " ":
#             answer += text
#             count = 0
#             continue
#
#         answer += text if count != 0 else text.upper()
#         count += 1
#
#     return answer