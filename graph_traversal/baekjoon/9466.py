import sys
sys.setrecursionlimit(111111)

def dfs(x):
    visited[x] = True

    travel.append(x)
    next = arr[x]  # 다음 확인할 사람

    if visited[next]:
        if next in travel:  # 중복된 노드 발견
            result.extend(travel[travel.index(next):])
            return
    else:
        dfs(next)



for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())  # 학생 수
    arr = [0] + list(map(int, sys.stdin.readline().split()))  # 선택한 번호
    visited = [True] + [False] * n
    result = list() # 팀이된 노드를 저장

    for i in range(1, n + 1):
        if not visited[i]:
            travel = []
            dfs(i)
    print(n - len(result))


