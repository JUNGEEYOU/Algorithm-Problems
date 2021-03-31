import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
dict_ = defaultdict(int)
for _ in range(n):
    dict_[sys.stdin.readline().rstrip()] += 1

x = sorted([(k, v) for k, v in dict_.items()], key=lambda x: (-x[1], x[0]))
print(x[0][0])