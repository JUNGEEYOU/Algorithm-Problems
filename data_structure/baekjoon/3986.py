import sys

n = int(sys.stdin.readline().rstrip())
count = 0
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    st = []
    for c in x:
        if not st:
            st.append(c)
        elif st[-1] == c:
            st.pop()
        else:
            st.append(c)
    if not st:
        count += 1

print(count)
