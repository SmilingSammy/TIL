def solution(arr1, arr2):
    answer = []

    for elem1 in arr1:
        tmp = []

        for elem2 in zip(*arr2):
            result = sum([e1 * e2 for e1, e2 in zip(elem1, elem2)])
            tmp.append(result)
        answer.append(tmp)

    return answer