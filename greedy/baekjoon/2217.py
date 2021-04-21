import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
max_ = arr[0] * n
n -= 1
for i, a in enumerate(arr[1:]):
    if max_ < a * n:
        max_ = a * n
    n -= 1

print(max_)
