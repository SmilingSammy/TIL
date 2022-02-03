def solution(arr):
    size = len(arr)
    answer = [0, 0]  # 0, 1 count

    def compress(x, y, size):
        val = arr[x][y]

        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] == val:
                    continue

                size //= 2  # size compress
                # case
                compress(x, y, size)
                compress(x, y + size, size)
                compress(x + size, y, size)
                compress(x + size, y + size, size)

                return

        answer[val] += 1

    compress(0, 0, size)

    return answer