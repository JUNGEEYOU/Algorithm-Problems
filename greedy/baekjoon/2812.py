import sys
"""
 k개를 지워서 얻을 수 있는 가장 큰 수 구하기 
"""
n, k = map(int, sys.stdin.readline().split()) # n자리, k개 지우기
s = sys.stdin.readline().rstrip()

# 앞에 있는 숫자가 더 커야한다.
st =[]
for i in range(len(s)):
    # 새로들어온 수가 더 큰 경우 앞에있는것 지우기
    while st and k > 0 and st[-1] < s[i]:
        st.pop()
        k -= 1
    st.append(s[i])

print("".join(st[:len(st) - k]))
