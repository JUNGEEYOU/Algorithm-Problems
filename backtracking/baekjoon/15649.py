"""
 순열. 순서 고려
"""
import sys

n, m = map(int, sys.stdin.readline().split())

answer = []

def recursive():
    if len(answer) == m:
        print(*answer)
        return

    for i in range(1, n + 1):
        if i in answer:
            continue
        answer.append(i)
        recursive()
        answer.pop()

recursive()

