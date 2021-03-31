import sys

k, n = map(int, sys.stdin.readline().split())  # 랜선 수, 필요한 랜선 수
arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))

left = 1
right = max(arr)
result = 1

while left <= right:
    mid = (left + right) // 2   # 자르고자하는 길이
    total = 0
    for a in arr:
        total += a // mid

    if total >= n:   # mid가 너무 작은 경우
        result = mid
        left = mid + 1
    else:            # mid가  경우 큰
        right = mid - 1
print(result)


