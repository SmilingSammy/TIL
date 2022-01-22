import re

def solution(dartResult):
    darts = re.findall("(\d+)([SDT])([*#]?)", dartResult)
    formula_dict = {'S': 1, 'D': 2, 'T': 3}
    option_dict = {'*': 2, '#': -1, '': 1}

    for i, dart in enumerate(darts):
        score = pow(int(dart[0]), formula_dict[dart[1]])
        option = option_dict[dart[2]]

        if option == 2 and i > 0:
            darts[i - 1] *= 2

        darts[i] = score * option

    return sum(darts)