import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

arr = deque([i for i in range(1, n + 1)])
result = list()
while arr:
    arr.rotate(-k)
    result.append(arr.pop())

print("<" + ", ".join(map(str, result)) +">")