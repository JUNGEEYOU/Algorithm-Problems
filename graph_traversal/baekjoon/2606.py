import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())  # 컴퓨터 수
m = int(sys.stdin.readline().rstrip())  # 컴퓨터 연결
graph = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
dq = deque()
dq.append(1)
visit[1] = True

while dq:
    node = dq.popleft()
    for next in graph[node]:
        if not visit[next]:
            dq.append(next)
            visit[next] = True
            count += 1
print(count)