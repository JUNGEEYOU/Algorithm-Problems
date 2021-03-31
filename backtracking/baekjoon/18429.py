import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = []
visit = [False] * n
result = 0
def recursive():
    global result
    if len(answer) == n:
        total = 500
        for a in answer:
            total += (a - k)
            if total < 500:
                break
        else:
            result += 1
        return

    for i in range(len(arr)):
        if visit[i]:
            continue
        answer.append(arr[i])
        visit[i] = True
        recursive()
        answer.pop()
        visit[i] = False

recursive()
print(result)