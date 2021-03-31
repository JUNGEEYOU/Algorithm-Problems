import sys

n, m = map(int, sys.stdin.readline().split())
num = []

def recursion():
    if len(num) == m:
        print(*num)
        return
    for i in range(1, n + 1):
        if not num or num[-1] <= i:
            num.append(i)
            recursion()
            num.pop()

recursion()

