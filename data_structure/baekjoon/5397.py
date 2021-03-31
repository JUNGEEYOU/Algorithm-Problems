import sys
from collections import deque

def sol(x):
    arr = deque()
    now = 0
    for c in x:
        if c == "<":
            if now > 0:
                now -= 1
        elif c == ">":
            if len(arr) > now:
                now += 1
        elif c == "-":
            if arr and now >= 1:
                del arr[now - 1]
            if now > 0:
                now -= 1
        else:
            arr.insert(now, c)
            now += 1
    print(''.join(arr))

for _ in range(int(sys.stdin.readline().rstrip())):
    x = sys.stdin.readline().rstrip()
    sol(x)

