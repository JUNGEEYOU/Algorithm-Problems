import sys

def binary(target):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().split()))

arr.sort()
for i in range(m):
    print(binary(arr2[i]), end=" ")
