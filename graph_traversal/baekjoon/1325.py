import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

def bfs(x):
    count = 1
    dq = deque()
    dq.append(x)
    visit[x] = 1
    while dq:
        a = dq.popleft()
        for c in graph[a]:
            if visit[c] == 0:
                visit[c] = 1
                count += 1
                dq.append(c)
    return count


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)  # b를 해킹하면 a 해킹 가능

result = []
max_val = 0
for i in range(1, n + 1):
    visit = [0] * (n + 1)
    bfs_ =bfs(i)
    max_val = max(max_val, bfs_)
    result.append((bfs_, i))

print(*sorted([j for i, j in result if i == max_val]))



