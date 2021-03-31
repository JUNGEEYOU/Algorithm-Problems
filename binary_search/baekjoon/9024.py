import sys
import collections
from itertools import combinations

for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = map(int, sys.stdin.readline().split())  # k로 만드는 조합 구하기
    arr = list(map(int, sys.stdin.readline().split()))
    # k와 차이
    # 수의 차이
    dict_ = collections.defaultdict(int)
    for com in combinations(arr, 2):
        dict_[com[0] + com[1]] += 1
    left = 0
    right = int(1e9)
    result = 0
    while left <= right:
        mid = (left + right) // 2  # k와 차이
        if dict_[abs(k - mid)] != 0:
            right = mid - 1
            result = dict_[abs(k - mid)]
        else:
            left = mid + 1
    print(result)



