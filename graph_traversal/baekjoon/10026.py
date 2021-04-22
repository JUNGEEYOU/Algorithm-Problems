import sys
import copy
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append([c for c in sys.stdin.readline().rstrip()])

count = [0, 0]
graph_ = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] != 'O':
            count[0] += 1
            dq = deque()
            dq.append((i, j))
            res = graph[i][j]
            graph[i][j] = "O"
            while dq:
                x, y = dq.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == res:
                        graph[nx][ny] = "O"
                        dq.append((nx, ny))


for i in range(n):
    for j in range(n):
        if graph_[i][j] != 'O':
            count[1] += 1
            dq = deque()
            dq.append((i, j))
            res = graph_[i][j]
            graph_[i][j] = "O"
            while dq:
                x, y = dq.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if res != graph_[nx][ny]:
                        if res in ["R", "G"] and graph_[nx][ny] in ["R", "G"]:
                            graph_[nx][ny] = "O"
                            dq.append((nx, ny))
                    else:
                        graph_[nx][ny] = "O"
                        dq.append((nx, ny))

print(*count)




