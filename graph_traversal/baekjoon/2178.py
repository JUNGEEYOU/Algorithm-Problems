import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append([int(i) for i in sys.stdin.readline().rstrip()])

dq = deque()
dq.append((0, 0))
graph[0][0] = 2
while dq:
    x, y = dq.popleft()
    for d in range(4):
        nx = dx[d] + x
        ny = dy[d] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dq.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1] - 1)