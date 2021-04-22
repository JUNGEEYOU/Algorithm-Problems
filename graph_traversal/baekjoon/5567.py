import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()
dq.append((1, 0))
visit[1] = 1
ans = 0
while dq:
    x, d = dq.popleft()  # d는 깊이를 나타냄
    for c in graph[x]:
        if visit[c] == 0 and d <= 1:
            ans += 1
            visit[c] = 1
            dq.append((c, d + 1))

print(ans)
