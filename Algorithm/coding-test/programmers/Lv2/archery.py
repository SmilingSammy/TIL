from copy import copy


def solution(n, info):
    answer = [None, 0]
    queue = [[[0] * 11, 0, n]]

    while queue:
        score, order, arrows = queue.pop(0)

        # 1~10점 case 전부 탐색 or 화살이 없는 경우 --> 점수 계산
        if order == 11 or arrows == 0:
            if arrows:
                score[-1] += arrows

            gap = 0

            for i, s in enumerate(score):
                if info[i] == 0 and score[i] == 0:
                    continue

                gap = gap - (10 - i) if info[i] >= score[i] else gap + (10 - i)

            if answer[-1] < gap:
                answer = [score, gap]
            elif answer[-1] == gap and answer[0]:
                for i in range(10, -1, -1):
                    if answer[0][i] == score[i]:
                        continue
                    if answer[0][i] > score[i]:
                        break
                    else:
                        answer = [score, gap]
                        break

            continue

        # 해당 점수를 포기하는 경우 (비기거나, 적게 맞추거나 --> 그냥 0개 맞추는 것이 젤 best)
        queue.append([score, order + 1, arrows])

        # 해당 점수를 얻는 경우 (어피치 맞춘 횟수 + 1)
        if arrows >= info[order] + 1:
            tmp = copy(score)
            tmp[order] = info[order] + 1
            queue.append([tmp, order + 1, arrows - (info[order] + 1)])

    return answer[0] if answer[-1] != 0 else [-1]