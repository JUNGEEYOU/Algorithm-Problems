import sys

n = int(sys.stdin.readline()) # 센서 개수
k = int(sys.stdin.readline()) # 집중국 개수
arr = list(map(int, sys.stdin.readline().split()))  # 센서의 좌표
arr.sort()

if k >= n:   # k가 많으면 모든 곳에서 설치 가능
    print(0)
else:
    gap = list()
    # arr 사이의 갭 구하기
    for i in range(n - 1):
        gap.append((arr[i + 1] - arr[i]))
    gap.sort()
    # 갭중에서 가장 큰 것 부터 제거해서 그 나머지의 합 구하기
    while k - 1:
        gap.pop()
        k -= 1
    print(sum(gap))
