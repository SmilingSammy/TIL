from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    answer = 0

    for c in cities:
        c = c.lower()

        if c in cache:
            cache.remove(c)
            answer += 1
        else:
            answer += 5

        cache.append(c)

    return answer