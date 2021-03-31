import sys
import collections

n, m, v = map(int, sys.stdin.readline().split())  # 정점, 간선, 탐색 시작
graph = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

dfs_graph = []
bfs_graph = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(x):
    visit[x] = True
    dfs_graph.append(x)
    for next in graph[x]:
        if not visit[next]:
            dfs(next)

def bfs(x):
    dq = collections.deque()
    bfs_graph.append(x)
    dq.append(x)
    visit[x] = True
    while dq:
        node = dq.popleft()
        for next in graph[node]:
            if not visit[next]:
                dq.append(next)
                bfs_graph.append(next)
                visit[next] = True


dfs(v)
visit = [False for _ in range(n + 1)]
bfs(v)
print(*dfs_graph)
print(*bfs_graph)
