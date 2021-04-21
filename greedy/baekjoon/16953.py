import sys

a, b = map(int, sys.stdin.readline().split())
# a -> b로 만드는데
# 1. 2를 곱한다. 2. 1을 수의 가장 오른쪽에 추가한다.
ans = 0
flag = True
while b > a:
    if b % 2 == 0:
        b = b // 2
    else:
        if str(b)[-1] == '1':
            b = str(b)[:-1]
            b = int(b)
        else:
            flag = False
            break
    ans += 1

if not flag or b != a:
    print(-1)
else:
    print(ans + 1)
