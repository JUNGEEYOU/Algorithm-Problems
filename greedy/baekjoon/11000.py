import sys
import heapq

arr = list()

for _ in range(int(sys.stdin.readline().rstrip())):
    s, t = map(int, sys.stdin.readline().split())
    arr.append((s, t))
arr.sort()   # 먼저 시작되는 강의

hq = []
heapq.heappush(hq, arr[0][1])
result = 1
for i in range(1, len(arr)):
    min_ = heapq.heappop(hq)   # 지금까지 가장 빨리 끝나는 강의
    if min_ > arr[i][0]:       # 새로운 강의실을 생성해야하는 경우
        result += 1
        heapq.heappush(hq, min_)
    heapq.heappush(hq, arr[i][1])
print(result)
