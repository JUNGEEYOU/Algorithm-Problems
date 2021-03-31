"""
 조합. 순서 고려 안함
"""
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = []

def recursive(answer):
    if len(answer) == m:
        print(*answer)
    for i in arr:
        if not answer or answer[-1] < i:
            answer.append(i)
            recursive(answer)
            answer.pop()

recursive([])