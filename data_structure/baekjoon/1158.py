import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

arr = deque([i for i in range(1, n + 1)])
