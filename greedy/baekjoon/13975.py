import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(arr)
    result = 0
    while len(arr) != 1:
        fir = heapq.heappop(arr)
        sec = heapq.heappop(arr)
        result += (fir + sec)
        heapq.heappush(arr, fir + sec)
    print(result)