import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_ = 0

if n % 2 == 0:
    # 짝수면
    for i, j in zip(arr[:n // 2], arr[n - 1:: -1]):
        if max_ < i + j:
            max_ = i + j
else:
    for i, j in zip(arr[:n // 2], arr[n - 2:: -1]):
        if max_ < i + j:
            max_ = i + j
    if max_ < arr[-1]:
        max_ = arr[-1]

print(max_)