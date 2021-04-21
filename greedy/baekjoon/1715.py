import sys
import heapq

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

heapq.heapify(arr)
result = 0
while len(arr) != 1:
    fir = heapq.heappop(arr)
    sec = heapq.heappop(arr)
    result += (fir + sec)
    heapq.heappush(arr, fir + sec)

print(result)