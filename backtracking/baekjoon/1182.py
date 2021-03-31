import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
visit = [False] * n

def dfs(cnt):
    global result
    if cnt == n:
        total = 0
        flag = True
        for i, v in enumerate(visit):
            if v:
                flag = False
                total += arr[i]
        if total == s and not flag:
            result += 1
        return
    visit[cnt] = True
    dfs(cnt + 1)
    visit[cnt] = False
    dfs(cnt + 1)

dfs(0)
print(result)

