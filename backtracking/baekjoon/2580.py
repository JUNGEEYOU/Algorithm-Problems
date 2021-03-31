import sys
zero_list = []
arr = []
for i in range(9):
    x = list(map(int, sys.stdin.readline().split()))
    zero_list.extend([(i, j) for j in range(len(x)) if x[j] == 0])
    arr.append(x)
zero = len(zero_list)
result = []

def dfs():
    if len(result) == zero:
        return

    # 나의 가로, 나의 세로, 나의 사각형이 모두 합이 45
    flag_x = False
    flag_y = False
    for x, y in zero_list:
        for i in arr[x]:
            if i == 0:
                flag_x = True
                break
        for i in range(9):
            if arr[i][y] == 0:
                flag_y = True
                break



