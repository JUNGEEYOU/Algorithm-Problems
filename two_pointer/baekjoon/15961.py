import sys
from collections import defaultdict


n, d, k, c = map(int, sys.stdin.readline().split())  # 접시 수, 초밥의 가지수, 연속 접시 수, 쿠폰 번호
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.extend(arr)   # 원형이라서 2개를 이음
kinds = defaultdict(int)
kinds[c] += 1   # 쿠폰 먹음

left = 0
right = 0

# 맨 처음에 k 만큼만 초밥 먹기
while right - left != k:
    kinds[arr[right]] += 1
    right += 1

result = len(kinds)
while right < len(arr):
    result = max(result, len(kinds))
    kinds[arr[left]] -= 1
    if kinds[arr[left]] == 0:
        del kinds[arr[left]]
    kinds[arr[right]] += 1

    right += 1
    left += 1

print(result)

