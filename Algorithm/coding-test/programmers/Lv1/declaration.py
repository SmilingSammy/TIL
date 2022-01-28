def solution(id_list, report, k):
    report = list(map(lambda x: x.split(' '), set(report)))
    declare = {i: [] for i in id_list} # 유저별 신고한 명단
    bully = {i: 0 for i in id_list} # 유저별 신고 당한 횟수

    for r in report:
        declare[r[0]].append(r[1])
        bully[r[1]] += 1

    stopped = set() # 정지된 명단

    for user, count in bully.items():
        if count >= k:
            stopped.add(user)

    return [(len(set(declare[user]) & stopped)) for user in declare]