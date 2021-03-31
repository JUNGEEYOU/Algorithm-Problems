import sys

n = int(sys.stdin.readline().rstrip())

left = 0
right = n
result = 0
while left <= right:
    mid = (left + right) // 2
    res = mid * mid
    if res >= n:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
