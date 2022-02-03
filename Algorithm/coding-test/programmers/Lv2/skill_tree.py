import re


def solution(skill, skill_trees):
    s_dict = {s: i for i, s in enumerate(skill)}
    condition = '|'.join(s_dict.keys())
    count = 0

    for tree in skill_trees:
        trees = re.findall(condition, tree)
        trees = list(map(lambda x: s_dict[x], trees))

        if trees == list(range(len(trees))):
            count += 1

    return count