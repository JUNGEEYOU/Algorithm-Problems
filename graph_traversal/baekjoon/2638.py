import sys
from collections import deque
"""
주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간
"""
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    dq = deque()
    dq.append((0, 0))
    visit[0][0] = -1
    count = 0
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visit[nx][ny] == -1 or visit[nx][ny] >= 2:
                continue
            # 공기인 경우, 추가만
            if graph[nx][ny] == 0:
                dq.append((nx, ny))
                visit[nx][ny] = -1
                continue
            else:
                # 치즈인 경우, + 1넣어주고
                if visit[nx][ny] == 1:
                    visit[nx][ny] += 1
                    graph[nx][ny] = 0
                    count += 1
                else:
                    visit[nx][ny] += 1
    return count

n, m = map(int, sys.stdin.readline().split())  # 세로, 가로
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

ans = 0
while True:
    visit = [[0] * m for _ in range(n)]
    if not bfs():
        break
    else:
        ans += 1

print(ans)

