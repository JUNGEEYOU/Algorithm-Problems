import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
for i in range(n):
    x = sys.stdin.readline().rstrip()
    for c in x:
        graph[i].append(c)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            result.append(1)
            count += 1
            dq = deque()
            dq.append((i, j))
            graph[i][j] = '0'
            while dq:
                x, y = dq.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "1":
                        dq.append((nx, ny))
                        graph[nx][ny] = '0'
                        result[-1] += 1

result.sort()
print(count, *result, sep="\n")

