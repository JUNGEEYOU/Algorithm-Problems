import sys

def dfs(p, depth):
    if depth == 4:
        print(1)
        sys.exit()
    for c in graph[p]:
        if visit[c] == 0:
            visit[c] = 1
            dfs(c, depth + 1)
            visit[c] = 0


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    visit[i] = 1
    dfs(i, 0)
    visit[i] = 0
print(0)