import sys

n = int(sys.stdin.readline().rstrip())
w = [] * n
visit = [False] * (n + 1)
arr = []
ans = int(1e9)

for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

def dfs():
    if len(arr) == n:
        if w[arr[-1][0]][arr[0][0]] == 0:  # 처음으로 돌아가는 것 불가능
            return int(1e9)
        else:   # 돌아가는 것 가능
            return sum(j for i, j in arr) + w[arr[-1][0]][arr[0][0]]
    res = int(1e9)
    for i in range(n):
        if visit[i]:
            continue
        if not arr or w[arr[-1][0]][i] != 0:
            visit[i] = True
            arr.append((i, w[arr[-1][0]][i] if arr else 0))
            res = min(res, dfs())
            arr.pop()
            visit[i] = False
    return res


print(dfs())