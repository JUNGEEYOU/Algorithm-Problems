import sys

arr = list(map(int, sys.stdin.readline().split()))   # 정답
num = []
result = 0

def dfs(cnt):
    global result
    if cnt == 10:
        total = 0
        for i in range(10):
            if arr[i] == num[i]:
                total += 1
                if total >= 5:
                    result += 1
                    break
        return

    for i in range(1, 6):
        if cnt >= 2 and num[-1] == num[-2] == i:
            continue
        num.append(i)
        dfs(cnt + 1)
        num.pop()

dfs(0)
print(result)

