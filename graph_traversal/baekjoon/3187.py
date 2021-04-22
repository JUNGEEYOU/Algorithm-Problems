import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c = map(int, sys.stdin.readline().split())
graph = []
for _ in range(r):
    graph.append([i for i in sys.stdin.readline().rstrip()])
visit = [[0] * c for _ in range(r)]
k_total = 0  # 양
v_total = 0  # 늑대
for i in range(r):
    for j in range(c):
        if graph[i][j] in ['k', 'v'] and visit[i][j] == 0:
            k_ = 0
            v_ = 0
            dq = deque()
            dq.append((i, j))
            visit[i][j] = 1
            if graph[i][j] == "k":
                k_ += 1
            else:
                v_ += 1

            while dq:
                x, y = dq.popleft()
                for d in range(4):
                    nx = dx[d] + x
                    ny = dy[d] + y
                    if nx < 0 or ny < 0 or nx > r or ny > c:
                        continue
                    if graph[nx][ny] == "#" or visit[nx][ny] == 1:
                        continue
                    if graph[nx][ny] == "k":
                        k_ += 1
                    if graph[nx][ny] == "v":
                        v_ += 1
                    visit[nx][ny] = 1
                    dq.append((nx, ny))

            if k_ > v_:
                k_total += k_
            else:
                v_total += v_

print(k_total, v_total)






