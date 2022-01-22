def solution(n, arr1, arr2):
    result = []
    for x, y in zip(arr1, arr2):
        x = list((n-len(bin(x)[2:]))*"0" + bin(x)[2:])
        y = list((n-len(bin(y)[2:]))*"0" + bin(y)[2:])

        tmp = ''
        for e1, e2 in zip(x, y):
            val = int(e1) + int(e2)
            if val > 0:
                tmp += "#"
            else:
                tmp += " "

        result.append(tmp)

    return result