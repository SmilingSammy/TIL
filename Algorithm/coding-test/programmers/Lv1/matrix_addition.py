def solution(arr1, arr2):
    result = []
    for mat1, mat2 in zip(arr1, arr2):
        result.append([elem1 + elem2
                       for elem1, elem2 in zip(mat1, mat2)])
    return result