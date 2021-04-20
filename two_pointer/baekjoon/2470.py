import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0
right = n - 1

result = []
zero_sum = int(1e10)
while left != right:
    now_sum = arr[left] + arr[right]
    if zero_sum > abs(now_sum):
        zero_sum = abs(now_sum)
        result = [arr[left], arr[right]]

    if now_sum < 0:
        left += 1
    elif now_sum > 0:
        right -= 1
    elif now_sum == 0:
        break

print(*result)


