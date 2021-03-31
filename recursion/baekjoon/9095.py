import sys

t = int(sys.stdin.readline().rstrip())


def dfs(sum_):
    if sum_ == x:
        return 1
    count = 0
    for i in range(1, 4):
        if sum_ > x:
            continue
        count += dfs(sum_ + i)
    return count


for _ in range(t):
    x = int(sys.stdin.readline().rstrip())
    print(dfs(0))

