import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visit = [False] * (n + 1)
arr.sort()
num = []
nums = list()

def dfs(cnt):
    if cnt == m:
        print(*nums)
        return
    last = 0
    for i, a in enumerate(arr):
        if not visit[i] and last != a:
            nums.append(a)
            visit[i] = True
            last = a
            dfs(cnt + 1)
            nums.pop()
            visit[i] = False

dfs(0)

