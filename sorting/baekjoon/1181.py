import sys

arr = list()
for _ in range(int(sys.stdin.readline().rstrip())):
    arr.append(sys.stdin.readline().rstrip())
arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))
print("\n".join(arr))