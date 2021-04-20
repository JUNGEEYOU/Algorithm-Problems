def get_time(time):
    s = time.split(":")
    return int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])

def get_all_time(end, term):
    end = get_time(end)
    start = end - float(term) + 0.001
    return (start, end)

def solution(lines):
    """
    초당 최대 처리량
    :param lines: 오름차순. 응답 끝나는 시간
    :return:
    """
    answer = 0
    all_time = []
    for line in lines:
        a, b, c = line.split(" ")
        start, end = get_all_time(b, c.strip("s"))
        all_time.append((start, end))






    return answer

print(solution(lines= [
"2016-09-15 03:10:33.020 0.011s",
"2016-09-15 01:00:07.000 2s"
]))