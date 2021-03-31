import sys
arr = []
for _ in range(int(sys.stdin.readline().rstrip())):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))

now = 0
result = 0
for a in arr:
    if now <= a[0]:
        now = a[1]
        result += 1

print(result)


