import sys


n = int(sys.stdin.readline().rstrip())

if n == 1 or n == 3:
    print(-1)
else:
    ans = n // 5
    n %= 5   # 5 나머지
    if n in [1, 4]:
        ans += 2
    elif n == 2:
        ans += 1
    elif n == 3:
        ans += 3
    print(ans)

