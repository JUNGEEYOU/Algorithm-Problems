import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = 0
now = 0  # 누적 값 

for a in arr:
    now += a
    result += now

print(result)
