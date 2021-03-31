import sys
import bisect

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    b.sort()
    result = 0
    for i in a:
        res = bisect.bisect_left(b, i)
        result += res
    print(result)