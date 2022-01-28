def solution(lottos, win_nums):
    score = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    equal = len(set(lottos) & set(win_nums))
    zero_count = lottos.count(0)

    return [score[equal + zero_count], score[equal]]
