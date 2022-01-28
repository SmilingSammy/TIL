from collections import Counter
def solution(participant, completion):
    p_dict = Counter(participant)
    c_dict = Counter(completion)

    for key in participant:
        try:
            if p_dict[key] != c_dict[key]:
                return key
        except(KeyError):
            return key