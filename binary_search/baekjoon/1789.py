import sys


s = int(sys.stdin.readline().rstrip())

left = 1
right = 100000000
result = 0
while left <= right:
    mid = (left + right) // 2
    res = ((mid + 1) * mid) / 2
    if res > s:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)