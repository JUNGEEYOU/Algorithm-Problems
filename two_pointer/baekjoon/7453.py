import sys

n = int(sys.stdin.readline())
a, b, c, d = list(), list(), list(), list()

for _ in range(n):
    a_, b_, c_, d_ = map(int, sys.stdin.readline().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)
    d.append(d_)

ab = []
cd = []
for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])
        cd.append(-(c[i] + d[j]))

ab_ = 0
cd_ = 0
ab.sort()
cd.sort()

result = 0
while ab_ < n * n and cd_ < n * n:
    if ab[ab_] == cd[cd_]:
        result += 1
        ab_ += 1
        cd_ += 1

    elif ab[ab_] < cd[cd_]:
        ab_ += 1
    else:
        cd_ += 1

print(result)
