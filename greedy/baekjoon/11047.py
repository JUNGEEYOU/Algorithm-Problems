import sys

n, k = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr.sort(reverse=True)

result = 0
for a in arr:
    result += k // a
    k = k % a
    if k <= 0:
        break
print(result)