import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs():
    visit = [[False] * m for _ in range(n)]
    dq = deque()
    dq.append((0, 0))
    visit[0][0] = True
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if graph[nx][ny] == 0:  # 공기면
                visit[nx][ny] = True
                dq.append((nx, ny))
            else:  # 치즈면
                visit[nx][ny] = True
                cnt += 1
                graph[nx][ny] = 0
    return cnt




n, m = map(int, sys.stdin.readline().split()) # 가로, 세로
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

ans = 0
count = 0
while True:
    cnt = dfs()
    if cnt == 0:
        break
    else:
        count = cnt
        ans += 1

print(ans)
print(count)