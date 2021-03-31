import sys

def binary_search(x, a):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))

a.sort()
for i in b:
    print(binary_search(i, a))