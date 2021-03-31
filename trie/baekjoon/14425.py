import sys

n, m = map(int, sys.stdin.readline().split())  # 문자열 개수,

set_n = set()

for _ in range(n):
    set_n.add(sys.stdin.readline().rstrip())

count = 0
for _ in range(m):
    if sys.stdin.readline().rstrip() in set_n:
        count += 1
print(count)
