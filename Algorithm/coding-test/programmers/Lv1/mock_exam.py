def solution(answers):
    p1, p2, p3 = '12345', '21232425', '3311224455'
    p1, p2, p3 = [p * (10000 // len(p)) for p in [p1, p2, p3]]

    counts = [[n, 0] for n in range(1, 4)]
    answers = ''.join(map(str, answers))

    for i in range(len(answers)):
        if answers[i] == p1[i]:
            counts[0][1] += 1
        if answers[i] == p2[i]:
            counts[1][1] += 1
        if answers[i] == p3[i]:
            counts[2][1] += 1

    _, count = zip(*counts)
    max_count = max(count)

    result = list(filter(lambda x: x[1] == max_count, counts))
    return sorted([r[0] for r in result])


# def solution(answers):
#     size = len(answers)
#     ansNo1 = [1, 2, 3, 4, 5] * int(10000 / 5)
#     ansNo2 = [2, 1, 2, 3, 2, 4, 2, 5] * int(10000 / 8)
#     ansNo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int(10000 / 10)
#
#     ans_dict = {key: 0 for key in [1,2,3]}
#     for idx in range(len(answers)):
#         if answers[idx] == ansNo1[idx]:
#             ans_dict[1] += 1
#         if answers[idx] == ansNo2[idx]:
#             ans_dict[2] += 1
#         if answers[idx] == ansNo3[idx]:
#             ans_dict[3] += 1
#
#     max_key = list(filter(lambda x : x[1] == max(ans_dict.values()), ans_dict.items()))
#     return sorted(list(map(lambda x : x[0], max_key)))