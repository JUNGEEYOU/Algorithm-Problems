import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split()) # 수빈, 동생 위치
visit = [[-1, []]] * 100001

dq = deque()
dq.append(n)
visit[n] = [0, [n]]

while dq:
    now = dq.popleft()
    if now * 2 <= 100000 and visit[now * 2][0] == -1:
        visit[now * 2][0] = visit[now][0] + 1
        visit[now * 2][1].extend(visit[now][1] + [now * 2])
        dq.append(now * 2)
    if now + 1 <= 100000 and visit[now + 1][0] == -1:
        visit[now + 1][0] = visit[now][0] + 1
        visit[now + 1][1].extend(visit[now][1] + [now + 1])
        dq.append(now + 1)
    if now - 1 >= 0 and visit[now - 1][0] == -1:
        visit[now - 1][0] = visit[now][0] + 1
        visit[now - 1][1].extend(visit[now][1] + [now - 1])
        dq.append(now - 1)

print(visit[k])
