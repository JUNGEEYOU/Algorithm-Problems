import sys

s = sys.stdin.readline().rstrip()

s = s.replace("XXXX", "AAAA")
s = s.replace("XX", "BB")

if s.find("X") != -1:
    print(-1)
else:
    print(s)


