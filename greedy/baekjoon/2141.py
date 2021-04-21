import sys


n = int(sys.stdin.readline())
arr = []
count = 0  # 전체 사람 수
for _ in range(n):
    # 마을 위치, 사람 수
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
    count += b

half = count / 2 # 중간 사람 수
now = 0
arr.sort()

# 중간 사람 수 위치에 살고 있는 위치 구하기
for pos, val in arr:
    now += val
    if now >= half:
        print(pos)
        break

