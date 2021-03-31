import sys

n, l = map(int, sys.stdin.readline().split())   # 물 새는 개수, 테이브 길이
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 1
start = arr[0]
end = arr[0] + l
for i in range(1, n):
    if start <= arr[i] < end:
        continue
    else:
        start = arr[i]
        end = arr[i] + l
        cnt += 1
print(cnt)
