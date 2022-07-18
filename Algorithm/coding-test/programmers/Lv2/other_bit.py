def solution(numbers):
    answer = []
    for number in numbers:
        num = list('0' + bin(number)[2:])
        idx = ''.join(num).rfind('0')
        num[idx] = '1'

        if number % 2 == 1:
            num[idx + 1] = '0'

        answer.append(int(''.join(num), 2))

    return answer