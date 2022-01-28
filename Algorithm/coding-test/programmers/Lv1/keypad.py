def solution(numbers, hand):
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    phone = sum(arr, [])

    left, right = '*', '#'
    answer = ''

    for n in numbers:

        if n in [1, 4, 7]:
            answer += 'L'
            left = n

        elif n in [3, 6, 9]:
            answer += 'R'
            right = n

        else:
            loc = divmod(phone.index(n), 3)
            l_loc = divmod(phone.index(left), 3)
            r_loc = divmod(phone.index(right), 3)

            # 거리 계산
            l_dist = sum([abs(x-y) for x, y in zip(loc, l_loc)])
            r_dist = sum([abs(x-y) for x, y in zip(loc, r_loc)])

            if l_dist < r_dist:
                answer += 'L'
                left = n
            elif l_dist > r_dist:
                answer += 'R'
                right = n
            else:
                if hand == 'right':
                    answer += 'R'
                    right = n
                else:
                    answer += 'L'
                    left = n

    return answer


# def solution(numbers, hand):
#     phone_ls = [[1,2,3], [4,5,6], [7,8,9], ["*",0,"#"]]
#     phone_dict = dict()
#     for i in range(len(phone_ls)):
#         for j in range(len(phone_ls[0])):
#             phone_dict[phone_ls[i][j]] = [i, j]
#
#     l_loc = "*"
#     r_loc = "#"
#
#     result = ""
#
#     for num in numbers:
#         if num in [1, 4, 7]:
#             result += "L"
#             l_loc = num
#
#         elif num in [3, 6, 9]:
#             result += "R"
#             r_loc = num
#
#         else:
#             num_loc = phone_dict[num]
#             l_dist = sum([abs(e1-e2) for e1, e2 in zip(num_loc, phone_dict[l_loc])])
#             r_dist = sum([abs(e1-e2) for e1, e2 in zip(num_loc, phone_dict[r_loc])])
#
#             if l_dist < r_dist or (l_dist == r_dist and hand == "left"):
#                 result += "L"
#                 l_loc = num
#
#             elif l_dist > r_dist or (l_dist == r_dist and hand == "right"):
#                 result += "R"
#                 r_loc = num
#
#     return result