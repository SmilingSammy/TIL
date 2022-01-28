import math


def time_to_minutes(time):
    time = time.split(":")

    return int(time[0]) * 60 + int(time[1])


def solution(fees, records):
    status = {}
    result = {}

    for r in records:
        time, car, state = r.split()  # 시간, 차량번호, 상태

        if state == 'IN':
            status[car] = time
        else:
            in_time = status.pop(car)
            in_time = time_to_minutes(in_time)
            out_time = time_to_minutes(time)

            if car not in result:
                result[car] = 0

            result[car] += out_time - in_time

    if status:
        for car in status:
            in_time = status[car]
            in_time = time_to_minutes(in_time)

            if car not in result:
                result[car] = 0

            result[car] += 1439 - in_time  # '23:59': 1439분

    answer = []

    for car in sorted(result.keys()):
        usage = result[car]  # 총 사용 시간
        total_cost = fees[1] + math.ceil(max(0, usage - fees[0]) / fees[2]) * fees[
            3]  # fees >> 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
        answer.append(total_cost)

    return answer
