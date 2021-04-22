import sys
from collections import deque

dx = [-1, 1, 2, 2, 1, -1, -2, -2 ]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]

for _ in range(int(sys.stdin.readline().rstrip())):
    l = int(sys.stdin.readline().rstrip())   # 한변의 길이
    graph = [[0] * l for _ in range(l)]
    x, y = map(int, sys.stdin.readline().split())  # 현재
    x_, y_ = map(int, sys.stdin.readline().split())  # 목표
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 1
    while dq:
        x, y = dq.popleft()
        if x == x_ and y == y_:
            print(graph[x][y] - 1)
            break
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                dq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
