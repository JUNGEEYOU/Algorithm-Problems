import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
for res in permutations(range(1, n + 1), n):
    print(*res)