import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)
total = arr[0]

for a in arr[1:]:
    total += a / 2

print(total)