import sys

def recursive(n, sum_, cnt_):
    if sum_ == n:
        return cnt_ + 1
    for i in range(1, 4):
        if sum_ > n:
            continue
        recursive(n, sum_ + i, cnt_)

arr = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    print(recursive(x, 0, 0))
