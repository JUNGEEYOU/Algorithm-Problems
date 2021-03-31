import sys


def check(n, m):
    cnt = 0
    for i in range(n, m + 1):
        arr = [0] * 10
        for c in str(i):
            arr[int(c)] += 1
            if arr[int(c)] > 1:
                break
        else:
            cnt += 1
    return cnt


while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
        print(check(n, m))
    except:
        break
