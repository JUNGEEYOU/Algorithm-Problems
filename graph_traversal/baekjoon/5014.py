import sys
from collections import deque
# 고층, 현재 위치, 스타링크, 위로 올라가는 버튼, 내려가는 버튼 
F, S, G, U, D = map(int, sys.stdin.readline().split())

visit = [-1] * (F + 1)
dq = deque()
dq.append(S)
visit[S] = 0

while dq:
    now = dq.popleft()
    if now + U <= F and visit[now + U] == -1:
        visit[now + U] = visit[now] + 1
        dq.append(now + U)

    if now - D >= 1 and visit[now - D] == -1:
        visit[now - D] = visit[now] + 1
        dq.append(now - D)
if visit[G] == -1:
    print("use the stairs")
else:
    print(visit[G])