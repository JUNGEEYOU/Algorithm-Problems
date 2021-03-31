import sys

def sol(n):
    if n < 2:
        return n
    else:
        return sol(n - 1) + sol(n - 2)


n = int(sys.stdin.readline().rstrip())
print(sol(n))