import sys


n, c = map(int, sys.stdin.readline().split())  # 집 수, 공유기 수
arr = [int(sys.stdin.readline().rstrip()) for i in range(n)]
arr.sort()

def cnt(mid):
    pre = arr[0]
    result = 1
    for i in range(1, n):
        if arr[i] - pre >= mid:
            result += 1
            pre = arr[i]
    return result


left = 0
right = arr[-1] - arr[0]
ans = 0
while left <= right:
    mid = (left + right) // 2

    if cnt(mid) >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)