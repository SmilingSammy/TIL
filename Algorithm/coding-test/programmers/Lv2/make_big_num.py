def solution(number, k):
    num_ls = list(number)

    stack = [num_ls[0]]

    for num in num_ls[1:]:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()

        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)