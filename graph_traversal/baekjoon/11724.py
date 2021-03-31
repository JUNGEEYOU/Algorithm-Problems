import sys
sys.setrecursionlimit(10000)  # 재귀관련 설정

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visit[x] = True
    for next in graph[x]:
        if not visit[next]:
            dfs(next)
count = 0
for i in range(1, n + 1):
    if not visit[i]:
        count += 1
        dfs(i)

print(count)


