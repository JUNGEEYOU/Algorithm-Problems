import sys

n, k = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

left = 1
right = max(arr) + k
result = 1
while left <= right:
    mid = (left + right) // 2   # 예측 최대 레벨
    total = 0
    for a in arr:
        if mid > a:
            total += mid - a
    if total <= k:   # 낮은 예측을 한 경우
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)

