import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


dq = deque()
dq.append(1)

while dq:
    p = dq.popleft()
    for c in graph[p]:
        if parents[c] == 0:
            parents[c] = p
            dq.append(c)


for i in parents[2:]:
    print(i)
