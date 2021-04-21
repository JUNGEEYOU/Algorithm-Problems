import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort(reverse=True)
total = 0

for i, a in enumerate(arr):
    x = (a - i)
    if x > 0:
        total += x
print(total)
