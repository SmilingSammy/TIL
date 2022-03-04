def solution(word):
    moeum_dict = {k: i for i, k in enumerate(['A', 'E', 'I', 'O', 'U'])}

    counts = [0]

    for v in range(5):
        val = 5 ** v + counts[-1]
        counts.append(val)

    counts.sort(reverse=True)
    counts.pop()

    answer = 0
    for i, w in enumerate(list(word)):
        answer += moeum_dict[w] * counts[i] + 1

    return answer