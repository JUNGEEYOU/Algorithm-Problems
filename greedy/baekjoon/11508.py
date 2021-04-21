import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)
left = 0
right = 3
total = 0
while n >= 3:
    n -= 3
    a = list(map(int, arr[left:right]))
    total += (a[1] + a[0])
    left += 3
    right += 3

while n:
    total += arr[-1]
    arr.pop()
    n -= 1


print(total)