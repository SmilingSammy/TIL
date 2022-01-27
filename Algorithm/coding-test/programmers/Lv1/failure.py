def solution(N, stages):

    p_num = len(stages) # 참가자 수
    fail_dict = {stg:0 for stg in range(1, N+1)} # stage별 멈춘 사람 수
    stg_dict = {} # stage별 멈춘 사람 수

    for stg in stages:
        if stg not in stg_dict:
            stg_dict[stg] = 0
        stg_dict[stg] += 1

    for stg in fail_dict:
        if stg not in stg_dict:
            continue
        fail_dict[stg] = stg_dict[stg] / p_num
        p_num -= stg_dict[stg]

    result = sorted(fail_dict.items(), key=lambda x: x[1], reverse=True)

    return [r[0] for r in result]
