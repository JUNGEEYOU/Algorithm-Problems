import sys
import itertools

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
cal_tmp = list(map(int, sys.stdin.readline().split()))  # 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
cal = list()
min_result = int(1e10)
max_result = -int(1e10)

for i, t in enumerate(cal_tmp):
    if t > 0:
        cal.extend([i] * t)

for res in itertools.permutations(cal, n - 1):
    result = arr[0]
    for r, a in zip(res, arr[1:]):
        if r == 0:
            result = result + a
        elif r == 1:
            result = result - a
        elif r == 2:
            result = result * a
        else:
            if result < 0:
                result = -(abs(result) // a)

            else:
                result = result // a

    min_result = min(min_result, result)
    max_result = max(max_result, result)

print(max_result)
print(min_result)
