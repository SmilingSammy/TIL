def solution(price, money, count):
    total = price * count * (count + 1) / 2
    remain = total - money

    return 0 if remain <= 0 else remain