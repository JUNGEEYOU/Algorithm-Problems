import sys
import bisect

def count(arr, right, left):
    return bisect.bisect_right(arr, right) - bisect.bisect_left(arr, left)

n, m = map(int, sys.stdin.readline().split())  # 점, 선분
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(count(arr, y, x))
