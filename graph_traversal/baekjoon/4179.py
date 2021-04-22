import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c = map(int, sys.stdin.readline().split())  # 행, 열
fire = []
graph = []
# hoon = ()
for j in range(r):
    x = [i for i in sys.stdin.readline().rstrip()]
    h = [(j, i) for i, c in enumerate(x) if c == "J"]
    if h:
        hoon = h[0]
    f = [(j, i) for i, c in enumerate(x) if c == "F"]
    if f:
        fire.extend(f)
    graph.append(x)


dq = deque()
dq.append(hoon)
dq.extend(fire)

while dq:
    x, y = dq.popleft()
    for d in range(4):
        nx = dx[d] + x
        ny = dy[d] + y
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            continue
        if graph[nx][ny] != ".":
            continue
        if graph[x][y] == "F":
            graph[nx][ny] = "F"
        elif graph[x][y] == "J":
            graph[nx][ny] = 2
        else:
            graph[nx][ny] = graph[x][y] + 1
        dq.append((nx, ny))

result = []
for i, g in enumerate(graph[r - 1]):
    if type(g) is int:
        result.append(graph[r - 1][i])

for i, g in enumerate(graph[0]):
    if type(g) is int:
        result.append(graph[0][i])

for i in range(r):
    for j in range(1):
        if type(g) is int:
            result.append(graph[i][j])

for i in range(r):
    for j in range(c - 1):
        if type(g) is int:
            result.append(graph[i][j])

result.sort()
if result:
    print(result[0])
else:
    print("IMPOSSIBLE")


