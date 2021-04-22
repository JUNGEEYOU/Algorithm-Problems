import sys
from collections import deque


dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    land = 0
    dq = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                land += 1
                dq.append((i, j))
                graph[i][j] = 0
                while dq:
                    x, y = dq.popleft()
                    for d in range(8):
                        nx = dx[d] + x
                        ny = dy[d] + y
                        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                            dq.append((nx, ny))
                            graph[nx][ny] = 0
    print(land)


