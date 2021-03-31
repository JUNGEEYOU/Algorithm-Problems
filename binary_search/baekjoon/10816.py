import sys
import bisect

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))

print(*[bisect.bisect_right(a, i) - bisect.bisect_left(a, i) for i in b])