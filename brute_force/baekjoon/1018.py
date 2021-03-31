import sys

n, m = map(int, sys.stdin.readline().split())
arr =[]

for _ in range(n):
    str_ = sys.stdin.readline().rstrip()
    arr.append([a for a in str_])


def check(i_s, j_s, start):
    """
     변경된 체스 수
    :param i: 행 시작
    :param j: 열 시작
    :param start: 시작 보드 값
    :return:
    """
    count = 0
    first = start
    for i in range(i_s, i_s + 8):
        now = first
        for j in range(j_s, j_s + 8):
            if arr[i][j] != now:
                count += 1
            now = "B" if now == "W" else "W"
        first = "B" if first == "W" else "W"
    return count
# 8 * 8 씩 잘라서 이동하기
result = int(1e9)
for i in range(0, n - 8 + 1):
    for j in range(0, m - 8 + 1):
        for start in ["W", "B"]:
            result = min(result, check(i, j, start))

print(result)
