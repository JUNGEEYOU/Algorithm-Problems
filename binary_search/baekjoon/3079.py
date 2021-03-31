import sys

n, m = map(int, sys.stdin.readline().split())   # 입국심사대, 사람
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

left = 1
right = m * max(arr)
result = 1
while left <= right:
    mid = (left + right) // 2  # 예측 시간
    total = 0
    for a in arr:
        total += (mid // a)
    if total >= m:
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)
