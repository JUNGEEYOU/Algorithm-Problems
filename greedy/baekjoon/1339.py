import sys

dict_ = dict()
for _ in range(int(sys.stdin.readline().rstrip())):
    a = sys.stdin.readline().rstrip()
    for i in range(0, len(a)):
        dict_.setdefault(a[i], 0)
        dict_[a[i]] += 10 ** (len(a) - i - 1)

result = sorted(dict_.values(), reverse=True)
num = 9
ans = 0
for res in result:
    ans += res * num
    num -= 1
print(ans)
