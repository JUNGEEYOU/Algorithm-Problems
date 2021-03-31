import sys

n, m = map(int, sys.stdin.readline().split())  # n개 수, m개 이하 구간
arr = list(map(int, sys.stdin.readline().split()))

# 구간 m개 이하로 만들어 최대값 - 최소값에서 최댓값 중 최소값 찾기