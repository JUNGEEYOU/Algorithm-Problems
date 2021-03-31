import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
ans = 9999999999
for i in range(n):
    graph[i + 1].extend([0] + list(map(int, sys.stdin.readline().split())))

for comb in combinations(range(1, n + 1), n // 2):
    # 팀 나누기
    team1 = list(comb)
    team2 = list()
    for a in range(1, n + 1):
        if a not in team1:
            team2.append(a)
    # 능력치 계산하기
    team1_s = 0
    team2_s = 0
    for i in range(0, n // 2 - 1):
        for j in range(i + 1, n // 2):
            team1_s += graph[team1[i]][team1[j]] + graph[team1[j]][team1[i]]
            team2_s += graph[team2[i]][team2[j]] + graph[team2[j]][team2[i]]
    ans = min(ans, abs(team2_s - team1_s))

print(ans)
