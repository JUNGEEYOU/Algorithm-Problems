import sys

n, c = map(int, sys.stdin.readline().split())  # 마을 수, 트럭 용량
m = int(sys.stdin.readline())  # 보내는 박스 정보수
arr = []
for _ in range(m):
    a, b, x = map(int, sys.stdin.readline().split())  # a-> b 박스수
    arr.append((a, b, x))

arr.sort(key=lambda x: x[1])  # 받는 마을 순으로
remains = [c for _ in range(n + 1)]  # 각 마을에서 가능한 적재량
ans = 0

for i in range(m):
    start, end, cnt = arr[i]
    # 구간에서의 가능 적재량이 최소인값을 찾기 + 현재 적재해야할 박스 : 최소인 것 중 찾아야 가능
    temp = c
    for j in range(start, end):
        temp = min(temp, remains[j])
    temp = min(temp, cnt)
    # 최소 가능 적재량을 빼주기
    for j in range(start, end):
        remains[j] -= temp
    ans += temp

print(ans)











