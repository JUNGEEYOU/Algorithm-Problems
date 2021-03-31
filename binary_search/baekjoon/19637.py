import sys

def binary_search(left, right, x):
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid][0] >= x:
            left = mid + 1
        else:
            res = mid
            right = mid - 1
    return res

n, m = map(int, sys.stdin.readline().split())  # n개의 칭호, m명
arr = []
for _ in range(n):
    x, y = map(str, sys.stdin.readline().split())
    arr.append((int(y), x))

for _ in range(m):
    a = int(sys.stdin.readline().rstrip())
    print(arr[binary_search(left=0, right=n - 1, x=a)][1])


