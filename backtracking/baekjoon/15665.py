import sys

n, m = map(int, sys.stdin.readline().split())
list_ = list(map(int, sys.stdin.readline().split()))
list_.sort()
arr = list()

def dfs():
    if len(arr) == m:
        print(*arr)
        return
    last = 0
    for i, a in enumerate(list_):
        if last != a:
            arr.append(a)
            last = a
            dfs()
            arr.pop()

dfs()