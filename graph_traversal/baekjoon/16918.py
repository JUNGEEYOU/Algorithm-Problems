import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def check():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                graph[i][j] = -1
                dq = deque()
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < r and 0 <= ny < c:
                            graph[nx][ny] = -1
            elif graph[i][j] > 1:
                graph[i][j] -= 1


def print_graph():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                print(".", end="")
            else:
                print("0", end="")
        print()


r, c, n = map(int, sys.stdin.readline().split())  # r줄 ,n초 후 결과
graph = list()



for _ in range(r):
    graph.append([3 if i =='O' else -1 for i in sys.stdin.readline().rstrip()])


while n:
    # # 1초 동안 아무것도 안함 - 1초
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1:  # 폭탄이면 -1
                graph[i][j] -= 1
    n -= 1
    if n <= 0:
        break
    check()
    # 폭탄이 안설치된 칸에 폭탄 설치 - 1초
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1:  # 폭탄이면 -1
                graph[i][j] -= 1
            else:
                graph[i][j] = 3    # 빈곳에 폭탄 설치
    check()
    n -= 1



print_graph()



