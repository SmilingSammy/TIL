import sys


def check(x):
    for y in range(x):
        if row[x] == row[y] or abs(row[x] - row[y]) == abs(x - y):
            return False

    return True


def queen(x):
    global count

    if x == N:
        count += 1
    else:
        for i in range(N):
            row[x] = i
            result = check(x)

            if result:
                queen(x + 1)

# Pypy3으로 풀어야 시간 초과 해결됨
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    count = 0
    row = [0 for _ in range(N)]

    queen(0)
    print(count)