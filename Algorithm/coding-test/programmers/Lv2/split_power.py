from collections import defaultdict


def dfs(x, visit):
    visit.append(x)  # add visit

    # add count number
    global count
    count += 1

    for node in tree[x]:
        if node not in visit:
            dfs(node, visit)


def solution(n, wires):
    global tree, count

    tree = defaultdict(list)
    result = []

    # make tree
    for x, y in wires:
        tree[x].append(y)
        tree[y].append(x)

    for x, y in wires:
        # cut node
        tree[x].remove(y)
        tree[y].remove(x)

        #
        count = 0
        dfs(1, [])

        # add node
        tree[x].append(y)
        tree[y].append(x)

        result.append(abs(n - count - count))

    return min(result)