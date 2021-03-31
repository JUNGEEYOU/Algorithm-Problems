import sys
from collections import Counter

arr = list()
for i in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline()))
print(round(sum(arr)/len(arr)))            # 산술평균 : N개의 수들의 합을 N으로 나눈 값
arr.sort()
print(arr[len(arr)//2])                    # 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
if len(arr) > 1:
    counter_dict = Counter(arr)
    most = counter_dict.most_common()
    if most[0][1] == most[1][1]:
        print(most[1][0])  # 두 번째로 작은 값
    else:
        print(most[0][0])
else:
    print(arr[0])

print(max(arr) - min(arr))                 # 범위 : N개의 수들 중 최댓값과 최솟값의 차이