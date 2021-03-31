import sys
n, m = map(int, sys.stdin.readline().split())  # 비번 길이, 비번 수
arr = list(map(int, sys.stdin.readline().split()))  # 선경지명 비번

nums = list()

def dfs():
    if len(nums) == n:
        for k in arr:
            if k not in nums:
                return 0
        return 1
    count = 0
    for i in range(0, 10):
        nums.append(i)
        count += dfs()
        nums.pop()
    return count

print(dfs())



