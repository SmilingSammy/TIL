from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)

    boat_count = 0

    while people:
        weight = people.popleft()
        if people and people[-1] <= limit - weight:
            weight += people.pop()
        boat_count += 1

    return boat_count