import sys

n, m = map(int, sys.stdin.readline().split())  # 수의 개수, 합
arr = list(map(int, sys.stdin.readline().split()))
pre = [0, arr[0]]

for i in range(1, n):
    pre.append(pre[i] + arr[i])
    arr[0]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(pre[e] - pre[s - 1])
