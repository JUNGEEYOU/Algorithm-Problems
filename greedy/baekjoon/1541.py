import sys

s = sys.stdin.readline().rstrip().split('-')
arr = list()
for i in range(len(s)):
    x = str(s[i]).split("+")
    res = 0
    for c in x:
        res += int(c)
    arr.append(res)

total = arr[0]
for i in arr[1:]:
    total -= i

print(total)

