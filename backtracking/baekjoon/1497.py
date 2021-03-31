import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
visit = [False] * n
result = []
all_n = True
for _ in range(n):
    _, b = map(str, sys.stdin.readline().split())
    if all_n:
        for i in b:
            if i == "Y":
                all_n = False
                break
    arr.append(b)

def dfs(cnt):
    global result
    if cnt == n:   # 모든 기타의 유무를 표시한 경우
        song = [False] * m   # 곡에 대한 유무
        count = 0
        for i, v in enumerate(visit):
            if v:       # 만약 방문한 경우인 경우
                count += 1
                for j, a in enumerate(arr[i]):
                    if a == "Y":  # 만약 연주할수 있는 곡인 경우
                        song[j] = True
        song_cnt = 0
        for t in song:   # 모든 곡이 True인 경우를 확인
            if t:
                song_cnt += 1
        result.append((song_cnt, count))
        return
    visit[cnt] = True
    dfs(cnt + 1)
    visit[cnt] = False
    dfs(cnt + 1)


if not all_n:
    dfs(0)
    result.sort(key=lambda x: (-x[0], x[1]))
    print(result[0][1])
else:
    print(-1)
