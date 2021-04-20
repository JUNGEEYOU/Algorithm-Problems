import sys


n, s = map(int, sys.stdin.readline().split())  # 합이 s이상
arr = list(map(int, sys.stdin.readline().split()))
prefix = [0]

# prefix 구하기
for i in range(n):
    prefix.append(prefix[i] + arr[i])

# s보다 작으면 right 이동, 크면 left 이동
left = 0
right = 1

min_len = int(1e10)
while left <= n:
    result = prefix[right] - prefix[left]
    if result < s:
        if right != n:
            right += 1
        else:
            left += 1
    elif result >= s:
        if min_len > right - left:
            min_len = right - left
        left += 1

if min_len == int(1e10):
    print(0)
else:
    print(min_len)
