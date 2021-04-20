import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())  # k개 이하로 포함하는 최장 연속 수열 길이
arr = list(map(int, sys.stdin.readline().split()))
dict_ = defaultdict(int)
left = 0
right = 0
result = 0
dict_[arr[left]] += 1

while left <= right and right < n:
    # 현재 right가 k개보다 커지면, right 값이 나올때까지 left +1
    if dict_[arr[right]] > k:
        dict_[arr[left]] -= 1
        left += 1
    else:
        result = max(result, right - left + 1)
        if right < n - 1:
            right += 1
            dict_[arr[right]] += 1
        else:
            break
print(result)