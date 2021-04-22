import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
# 이동 가능한 범위
dx = [0, 0, 1]
dy = [1, -1, k]
graph = []
visit = [[False] * (n + 1) for _ in range(2)]
# 1은 안전한 칸, 0은 위험한 칸
for _ in range(2):
    graph.append([int(i) for i in sys.stdin.readline().rstrip()])

dq = deque()
dq.append((0, 0, 0))

flag = False
visit[0][0] = True
while dq:
    x, y, c = dq.popleft()  # c는 시간 초
    for d in range(3):
        nx = dx[d] + x
        ny = dy[d] + y
        if d == 2:  # 마지막 행동은 2로 나눠준다.
            nx = nx % 2
        if ny >= n:  # 범위가 넘어가면 그만
            flag = True
            break
        # 방문한 적이 없고, 안전한 칸이고, c칸보다 큰 경우
        if not visit[nx][ny] and graph[nx][ny] == 1 and c < ny:
            dq.append((nx, ny, c + 1))  # 부모의 초에 + 1를 한다.
            visit[nx][ny] = True

if flag:
    print(1)
else:
    print(0)