import string


def solution(msg):
    dictionary = {k: (i+1) for i, k in enumerate(string.ascii_uppercase)} # 단어 사전
    idx_num = max(dictionary.values()) # 단어 번호
    answer = []; chg = False

    while msg != '':
        for i in range(1, len(msg)+1):
            if msg[:i] not in dictionary:
                idx_num += 1 # 단어 번호 갱신
                dictionary[msg[:i]] = idx_num # 새로운 단어 추가
                answer.append(dictionary[msg[:i-1]])
                chg = True; msg = msg[i-1:]
                break

        if not chg:
            answer.append(dictionary[msg])
            msg = ''

        chg = False

    return answer


# def solution(s):
#     idx_ls = []
#     last_num = 27
#     lzw_dict = {key: (num+1) for num, key in enumerate(list(string.ascii_uppercase))}
#
#     while s != '':
#         pos_case = list(filter(lambda x: x == s[:len(x)], lzw_dict.keys()))
#         w = sorted(pos_case, key=lambda x: len(x), reverse=True)[0]
#
#         # idx num append
#         idx_ls.append(lzw_dict[w])
#         # dict update
#         lzw_dict[s[:len(w)+1]] = last_num
#         last_num += 1
#         s = s[len(w):]
#
#     return idx_ls