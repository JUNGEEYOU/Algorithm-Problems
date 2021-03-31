import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())  # 가로 세로
graph = [[] for _ in range(n)]
date = 0

dq = deque()   # 1이 담긴 토마토의 위치
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    one = [(i, j) for j in range(m) if x[j] == 1]
    dq.extend(one)
    graph[i] = x

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return 0
    return 1   # 한개라도 0이 없는 경우

if check() == 1:
    print(0)
    sys.exit()
else:
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위에 벗어나는 경우
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 0이 아닌 경우
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                dq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                date = max(graph[nx][ny], date)

if check() == 0:
    print(-1)
else:
    print(date - 1)


