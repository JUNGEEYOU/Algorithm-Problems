import sys

n = int(sys.stdin.readline().rstrip())


def dfs(nums):
    if len(nums) == n:
        return 1
    count = 0
    for i in range(1, n + 1):
        flag = True
        for idx, val in enumerate(nums):
            if val == i:  # 같은 행에 존재하면 안됨
                flag = False
                break
            # 값의 차(열 차) == 인덱스 차(행 차)
            if abs(i - val) == len(nums) - idx:
                flag = False
                break
        if flag:
            nums.append(i)
            count += dfs(nums)
            nums.pop()
    return count

print(dfs([]))