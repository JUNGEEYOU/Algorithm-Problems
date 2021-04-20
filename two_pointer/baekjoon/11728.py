import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a_point = 0
b_point = 0
result = list()

while a_point < len(a) and b_point < len(b):
    if a[a_point] == b[b_point]:
        result.append(a[a_point])
        result.append(b[b_point])
        a_point += 1
        b_point += 1
    # b가 현재 더 큰 경우
    elif a[a_point] < b[b_point]:
        result.append(a[a_point])
        a_point += 1
    else:
        result.append(b[b_point])
        b_point += 1
if a_point < len(a):
    while a_point < len(a):
        result.append(a[a_point])
        a_point += 1

if b_point < len(b):
    while b_point < len(b):
        result.append(b[b_point])
        b_point += 1
print(*result)

