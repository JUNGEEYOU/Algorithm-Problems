import sys

n, m = map(int, sys.stdin.readline().split())
list_ = list(map(int, sys.stdin.readline().split()))
list_.sort()
arr = list()

def dfs():
    if len(arr) == m:
        print(*arr)
        return
    last = 0   # 1 9, 1 9 두 번 사용을 막기 위함
    for i, a in enumerate(list_):
        if last != a and (not arr or arr[-1] <= a):
            arr.append(a)
            last = a
            dfs()
            arr.pop()

dfs()
