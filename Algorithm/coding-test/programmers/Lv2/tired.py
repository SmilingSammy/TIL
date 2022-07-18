from itertools import permutations


def solution(k, dungeons):
    cases = list(permutations(range(len(dungeons)), len(dungeons)))
    candidates = []

    for case in cases:
        energy = k
        done = 0

        for c in case:
            minimum_energy, use_energy = dungeons[c]

            if (energy >= minimum_energy) and (energy >= use_energy):
                energy -= use_energy
                done += 1

        candidates.append(done)

    return max(candidates)