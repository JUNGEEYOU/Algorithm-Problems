import sys

def recursion(a):
    if a <= 1:
        return a
    else:
        return recursion(a - 1) * a

n = int(sys.stdin.readline().rstrip())
print(recursion(n))
