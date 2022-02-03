import re


def solution(m, musicinfos):
    # 분 계산
    get_minutes = lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1])
    # 결과
    result = []

    for info in musicinfos:
        start, end, title, song = info.split(',')
        start = get_minutes(start)  # 음악 시작
        end = get_minutes(end)  # 음악 종료
        time = end - start  # 연주 시간

        m_song = re.findall('[A-Z]{1}#{0,1}', m)  # 음표 추출
        song = re.findall('[A-Z]{1}#{0,1}', song)  # 음표 추출
        song = (song * (1439 // len(song) + 1))[:time]  # 1439개 이하 (조건)

        for i in range(len(song)):
            if song[i] != m_song[0]:
                continue
            if ''.join(song[i:i + len(m_song)]) == m:
                result.append([title, time])
                break

    return sorted(result, key=lambda x: x[1], reverse=True)[0][0] if result else '(None)'