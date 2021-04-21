import sys
import heapq

n = int(sys.stdin.readline())
arr = list()
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

# 시작 시간으로 정렬 - 앞부터 순서대로 배정
arr.sort()

hq = list()
heapq.heappush(hq, arr[0][1])  # 첫 회의실 배정, 끝나는 시간

for i in range(1, n):
    # 최소 끝나는 시간과 비교
    # 최소 끝나는 시간 <= 현재 강의 시작 시간  - 그대로 사용
    if hq[0] <= arr[i][0]:
        heapq.heappop(hq)
        heapq.heappush(hq, arr[i][1])

    else:
        heapq.heappush(hq, arr[i][1])
print(len(hq))
