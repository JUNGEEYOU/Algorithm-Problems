import sys

def binary(target):
    result = 0
    while target:
        result += target // 5
        target = target // 5
    return result

m = int(sys.stdin.readline().rstrip())  # 0의 개수가 m개
left = 5
right = 1000000000
ans = 0
while left <= right:
    mid = (left + right) // 2
    if binary(mid) >= m:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

if binary(ans) == m:
    print(ans)
else:
    print(-1)


