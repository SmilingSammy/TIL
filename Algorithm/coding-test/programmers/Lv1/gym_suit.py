def solution(n, lost, reserve):

    per_lost = list(set(lost) - set(reserve))
    per_res = list(set(reserve) - set(lost))

    cnt = len(per_lost)
    for elem in per_lost:
        if (elem-1) in per_res:
            per_res.remove(elem-1)
            cnt -= 1
        elif (elem+1) in per_res:
            per_res.remove(elem+1)
            cnt -= 1

    return n - cnt


# def solution(n, lost, reserve):
#     # 학생 체육복 수 dict
#     std_dict = {s: 1 for s in range(1, n+1)}
#
#     # 여분 학생 체육복 증가
#     for std in reserve:
#         std_dict[std] += 1
#
#     # 도난 학생 체육복 차감
#     for std in lost:
#         std_dict[std] -= 1
#
#     for std in std_dict:
#         if std_dict[std] != 0:
#             continue
#
#         front, back = std - 1, std + 1
#
#         if front in std_dict and std_dict[front] > 1:
#             std_dict[front] -= 1
#             std_dict[std] += 1
#             continue
#
#         if back in std_dict and std_dict[back] > 1:
#             std_dict[back] -= 1
#             std_dict[std] += 1
#             continue
#
#     return len(list(filter(lambda x: x > 0, std_dict.values())))