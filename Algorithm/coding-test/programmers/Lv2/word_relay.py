from collections import defaultdict


def solution(n, words):
    dictionary = defaultdict()
    before_word = words[0]
    dictionary[before_word] = 1

    for i in range(1, len(words)):
        word = words[i]

        if word in dictionary or before_word[-1] != word[0]:
            return [i % n + 1, i // n + 1]

        dictionary[word] = 1
        before_word = word

    return [0, 0]