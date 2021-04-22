import sys
from collections import deque

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(n)]
a, b = map(int, sys.stdin.readline().split())

arr = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x - 1, y - 1))

dq = deque()
dq.append((a - 1, b - 1))
graph[a - 1][b - 1] = 1

while dq:
    x, y = dq.popleft()
    for d in range(8):
        nx = dx[d] + x
        ny = dy[d] + y
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            dq.append((nx, ny))

for x, y in arr:
    print(graph[x][y] - 1, end=" ")
